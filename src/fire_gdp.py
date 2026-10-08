def get_data(file_name,
             query_column=None,
             query_value=None,
             return_header=False):
    results = []

    file = open(file_name, 'r')

    header = file.readline().strip().split(sep=',')

    # should we be converting to floats/ints??
    for line in file:
        entries = line.strip().split(sep=',')
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
