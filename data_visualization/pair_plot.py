#!/usr/bin/env -S uv run --script

import sys
sys.path.append("..")
sys.path.append(".")
sys.path.append("./data_analysis")

import matplotlib.pyplot as plt  # noqa: E402
import textwrap  as tw # noqa: E402

from pandas import read_csv, isna, DataFrame  # noqa: E402
from pandas.errors import EmptyDataError, ParserError  # noqa: E402

def pair_plot(data: DataFrame):
    """
    Args:
        values    (DataFrame): DataFrame of the parsed csv to compute
    """
    house_colors = {
        'Gryffindor': "#CE4646",
        'Hufflepuff': "#FFDA09",
        'Ravenclaw':  "#7186C9",
        'Slytherin':  "#18B850",
    }

    numeric = data.select_dtypes(include='number')
    numeric = numeric.drop(columns=['Index'], errors='ignore')

    cols = len(numeric.columns)
    fig, axes = plt.subplots(cols, cols, figsize=(12, 12))

    for i in range(cols):
        for j in range(cols):
            ax = axes[i, j]

            for house, color in house_colors.items():
                house_data = data[data['Hogwarts House'] == house]
                
                if i == j:
                    values = house_data[numeric.columns[i]].dropna()
                    ax.hist(values, bins=15, label=house, color=color, alpha=0.5)
                else:
                    x_vals = house_data[numeric.columns[j]]
                    y_vals = house_data[numeric.columns[i]]
                    ax.scatter(x_vals, y_vals, label=house, color=color, alpha=0.7, s=1)

            col_x_name = "\n".join(tw.wrap(numeric.columns[j], width=10))
            col_y_name = "\n".join(tw.wrap(numeric.columns[i], width=10))

            if j == 0:
                ax.set_ylabel(col_y_name, fontsize=8)
            if i == cols - 1:
                ax.set_xlabel(col_x_name, fontsize=8)

            ax.set_xticks([])
            ax.set_yticks([])

    plt.tight_layout(rect=[0, 0, 1, 0.93])
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(
        handles, 
        labels, 
        loc='center', 
        bbox_to_anchor=(0.5, 0.965), 
        fontsize=12, 
        ncol=4, 
        frameon=False
    )

    plt.show()

def main():
    if len(sys.argv) != 2:
        print("Usage: ./describe.py <file.csv>")
        return (1)
    try:
        data: DataFrame = read_csv(sys.argv[1])
        pair_plot(data)
    except FileNotFoundError:
        print("File " + sys.argv[1] + " don't exist")
        return (1)
    except IsADirectoryError:
        print(sys.argv[1] + " is a directory, not a file")
        return (1)
    except PermissionError:
        print("Permission denied in " + sys.argv[1])
        return (1)
    except EmptyDataError:
        print(sys.argv[1] + " is empty")
        return (1)
    except ParserError:
        print(sys.argv[1] + " is not a valid CSV file")
        return (1)
    except UnicodeDecodeError:
        print(sys.argv[1] + " has an invalid encoding")
        return (1)
    except KeyError as err:
        print(f"KeyError: {err} is not in " + sys.argv[1])
        return (1)
    except IOError:
        print("An error occured while accessing " + sys.argv[1])
        return (1)
    return (0)

if __name__ == "__main__":
    main()