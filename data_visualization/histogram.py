#!/usr/bin/env -S uv run --script

import sys
sys.path.append("..")
sys.path.append(".")
sys.path.append("./data_analysis")

import matplotlib.pyplot as plt  # noqa: E402

from pandas import read_csv, isna, DataFrame  # noqa: E402
from pandas.errors import EmptyDataError, ParserError  # noqa: E402

def histogram(data: DataFrame):
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
    courses = numeric.columns

    course_variances = []

    for col in courses:
        house_mean = data.groupby('Hogwarts House')[col].mean()
        current_variance = house_mean.var()

        if isna(current_variance):
            continue

        course_variances.append((col, current_variance))

        if not course_variances:
            raise ValueError("No data to analyse")

    course_variances.sort(key=lambda x: x[1])
    homogeneous_course = course_variances[0][0]

    for house, color in house_colors.items():
        house_data = data.loc[data['Hogwarts House'] == house, homogeneous_course].dropna()
        plt.hist(house_data, bins=15, alpha=0.5, label=house, color=color)

    plt.title(homogeneous_course)
    plt.xlabel('Notes')
    plt.ylabel('Frequency')
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    if len(sys.argv) != 2:
        print("Usage: ./describe.py <file.csv>")
        return (1)
    try:
        data: DataFrame = read_csv(sys.argv[1])
        histogram(data)
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