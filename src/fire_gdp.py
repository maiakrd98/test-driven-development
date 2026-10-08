import sys
import warnings


def get_data(file_name,
             query_column=None,
             query_value=None,
             return_header=False):

    if query_value is None and query_column is not None:
        sys.exit("You input a query_column, but not a query_value, please "
                 "enter either both or neither")
    if query_column is None and query_value is not None:
        sys.exit("You input a query_value, but not a query_column, please "
                 "enter either both or neither")

    results = []

    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        sys.exit("Could not find " + file_name)

    header = file.readline().strip().split(sep=',')

    query_value_exists = False

    # should we be converting to floats/ints??
    for line in file:
        entries = line.strip().split(sep=',')
        if query_column is not None:
            try:
                query_entry = entries[query_column]
            except IndexError:
                file.close()
                sys.exit('query_column index (' + str(query_column) +
                         ') is out of bounds')
        if query_column is None or query_entry == query_value:
            query_value_exists = True
            results.append(entries)

    file.close()

    if query_value is not None and not query_value_exists:
        warnings.warn("The query_value you entered ('" + query_value + "') is "
                      "not present", UserWarning)
        return None

    elif return_header:
        return header, results

    else:
        return results


def get_column_index(header, column_name):

    if header is None:
        warnings.warn("Warning: you have entered None as a header",
                      UserWarning)
        return None

    if len(header) == 0:
        warnings.warn("Warning: you have entered an empty header",
                      UserWarning)
        return None

    try:
        col_index = header.index(column_name)
    except ValueError:
        return None

    return col_index


def get_fire_gdp_year_data(co2_file,
                           gdp_file,
                           country,
                           emission_col_name="Forest fires"):

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        co2_info = get_data(co2_file,
                            query_column=0,
                            query_value=country,
                            return_header=True)
    if co2_info is None:
        warnings.warn("The country you entered ('" + country + "') is not "
                      "present in the co2_file ('" + co2_file + "')",
                      UserWarning)
        return None
    co2_header, co2_data = co2_info

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        gdp_info = get_data(gdp_file,
                            query_column=0,
                            query_value=country,
                            return_header=True)
    if gdp_info is None:
        warnings.warn("The country you entered ('" + country + "') is not "
                      "present in the gdp_file ('" + gdp_file + "')",
                      UserWarning)
        return None
    gdp_header, gdp_data = gdp_info

    results = []

    emission_col_index = get_column_index(co2_header, emission_col_name)

    for co2_row in co2_data:
        year = co2_row[1]
        emissions = co2_row[emission_col_index]
        gdp_year_col = get_column_index(gdp_header, year)
        gdp = gdp_data[0][gdp_year_col]
        if emissions != "":
            results.append([int(year), float(emissions), float(gdp)])

    return results
