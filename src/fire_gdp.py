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
            warnings.warn("Warning: you have entered None as a header", UserWarning)
            return None

    if len(header) == 0:
        warnings.warn("Warning: you have entered an empty header", UserWarning)
        return None

    try:
        col_index = header.index(column_name)
    except ValueError:
        return None

    return col_index


def get_fire_gdp_year_data(co2_file, gdp_file, country):
    pass
