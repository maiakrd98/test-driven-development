import sys
import warnings


def get_data(file_name,
             query_column=None,
             query_value=None,
             return_header=False):

    """ Opens a file and returns its entries as strings. If a query column \
    and value are given, it returns only the rows where the string in that \
    column matches the value. If return_header is True, it also return the \
    header.

    Parameters
    ----------
    file_name : str
        Name of file to be opened

    query_column : int, optional (default = None)
        Column to match to query_value

    query_value : str, optional (default = None)
        Desired value of query_column

    return_header : boolean, optional (default = False)
        If true, also return the header

    Returns
    -------
    results : list of lists of str
        List of lists, each of which is the entries in a row of the file

    header : list of str
        Only returned if return_header is True. List of the headers in a file
    """

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
    """ Finds the index of a column name in a header list. If the name is not \
    in the header, it returns None.

    Parameters
    ----------
    header : list of str
        Header to look for the column name in

    column_name : str
        Desired column name

    Returns
    -------
    col_index : int
        The index of column_name in header
    """

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
    """ Combines emissions and GDP for one country by matching years. \
    If emission_col_name is provided, it returns that emission type, \
    otherwise it returns forest fire emissions.

    Parameters
    ----------
    co2_file : str
        Path to file containing emission data

    gdp_file : str
        Path to file containing GDP data

    country : str
        Country you want data from

    emission_col_name : str, optional (default = "Forest fires")
        Emission column you want data from

    Returns
    -------
    results : list of lists [int, float, float]
        List of lists, each of which is [year, emissions, gdp] for the \
        given country
    """

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
    if emission_col_index is None:
        warnings.warn("There is no column in '" + co2_file +
                      "' titled '" + emission_col_name + "'",
                      UserWarning)
        return None

    for co2_row in co2_data:
        year = co2_row[1]
        emissions = co2_row[emission_col_index]
        gdp_year_col = get_column_index(gdp_header, year)
        gdp = gdp_data[0][gdp_year_col]
        if emissions != "" and gdp != "":
            try:
                int_year = int(year)
            except ValueError:
                sys.exit("Unable to convert '" + year + "' to int")
            try:
                float_emissions = float(emissions)
            except ValueError:
                sys.exit("Unable to convert '" + emissions + "' to float")
            try:
                float_gdp = float(gdp)
            except ValueError:
                sys.exit("Unable to convert '" + gdp + "' to float")
            results.append([int_year, float_emissions, float_gdp])

    return results
