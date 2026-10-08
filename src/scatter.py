import sys
import argparse
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(
                        prog='scatter',
                        description='Makes scatter plots') # improve this

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

    parser.add_argument('--x_axis_label',
                        type=str,
                        help='Label for x-axis',
                        required=True)

    parser.add_argument('--y_axis_label',
                        type=str,
                        help='Label for y-axis',
                        required=True)

    args = parser.parse_args()

    X = []
    Y = []
    for l in open(args.data_file):
        A = l.rstrip().split()
        X.append(float(A[0]))
        Y.append(float(A[1]))

    fig, ax = plt.subplots()
    ax.scatter(X,Y)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel(args.x_axis_label)
    ax.set_ylabel(args.y_axis_label)
    ax.set_title(args.title)

    plt.savefig(args.out_file,bbox_inches='tight')

if __name__ == "__main__":
    main()