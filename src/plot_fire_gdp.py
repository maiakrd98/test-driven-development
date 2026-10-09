import argparse
import sys
import warnings
import matplotlib.pyplot as plt
import fire_gdp


def main():
    parser = argparse.ArgumentParser(
                        prog='scatter',
                        description='Make a scatter plot of GDP vs a given '
                                    'emission type for a given country')

    parser.add_argument('--co2_file',
                        type=str,
                        help='File containing emissions data',
                        required=True)

    parser.add_argument('--gdp_file',
                        type=str,
                        help='File containing GDP data',
                        required=True)

    parser.add_argument('--out_file',
                        type=str,
                        help='File path to save plot',
                        required=True)

    parser.add_argument('--title',
                        type=str,
                        help='Plot title',
                        required=True)

    parser.add_argument('--y_variable',
                        type=str,
                        help="Variable to plot on the y-axis "
                             "(one of the headers of co2_file)",
                        required=True)

    parser.add_argument('--y_axis_label',
                        type=str,
                        help='Label for y-axis',
                        required=True)

    parser.add_argument('--country',
                        type=str,
                        help='Country to plot data for',
                        required=True)

    args = parser.parse_args()

    X = []
    Y = []

    with warnings.catch_warnings(record=True) as caught_warnings:
        warnings.simplefilter("always")
        fire_gdp_data = fire_gdp.get_fire_gdp_year_data(args.co2_file,
                                                        args.gdp_file,
                                                        args.country,
                                                        args.y_variable)
        warning_found = any("The country you entered ('" + args.country +
                            "') is not present" in str(w.message)
                            for w in caught_warnings)
        if warning_found:
            sys.exit(args.country + " is not a country in " + args.co2_file +
                     " and/or " + args.gdp_file)

    for row in fire_gdp_data:
        X.append(row[2])
        Y.append(row[1])

    fig, ax = plt.subplots()
    ax.scatter(X, Y)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel('GDP')
    ax.set_ylabel(args.y_axis_label)
    ax.set_title(args.title)

    plt.savefig(args.out_file, bbox_inches='tight')


if __name__ == "__main__":
    main()
