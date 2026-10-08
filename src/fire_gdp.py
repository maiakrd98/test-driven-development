import sys

def get_data(file_name,
             query_column=None,
             query_value=None,
             return_header=False):

    if query_value is None and query_column is not None:
        sys.exit("You input a query_column, but not a query_value, please "
                 "enter either both or neither")
    
    results = []

    file = open(file_name, 'r')

    header = file.readline().strip().split(sep=',')

    # should we be converting to floats/ints??
    for line in file:
        entries = line.strip().split(sep=',')
        if query_column is None or entries[query_column] == query_value:
            results.append(entries)

    file.close()

    if return_header:
        return header, results

    else:
        return results


def get_column_index(header, column_name):
    pass


def get_fire_gdp_year_data(co2_file, gdp_file, country):
    pass
