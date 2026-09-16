#!/usr/bin/env -S uv run --script

import sys
sys.path.append("..")
sys.path.append(".")
sys.path.append("./logistic_regression")
from datetime import datetime

from pandas import read_csv, DataFrame, Series  # noqa: E402
from math import exp, log
from pandas.errors import EmptyDataError, ParserError  # noqa: E402


def precision(base: DataFrame, prediction: DataFrame):
    precision = (base["Hogwarts House"] == prediction["Hogwarts House"]).sum()
    print((precision * 100) / len(base), "% accuracy")

def main():
    if len(sys.argv) != 3:
        print("Usage: ./precision.py <file.csv> house.csv")
        return (1)
    try:
        base: DataFrame = read_csv(sys.argv[1])
        prediction: DataFrame = read_csv(sys.argv[2], index_col=0)
        precision(base, prediction)
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