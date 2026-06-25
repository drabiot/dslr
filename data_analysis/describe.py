#!/usr/bin/env python3

import sys
sys.path.append("..")
sys.path.append(".")
sys.path.append("./data_analysis")

from pandas import read_csv, DataFrame  # noqa: E402
from pandas.errors import EmptyDataError, ParserError  # noqa: E402
from dslr_lib.functions import (  # noqa: E402
    ft_count,
    ft_mean,
    ft_std,
    ft_min,
    ft_quantile,
    ft_max,
)


def describe(data: DataFrame) -> DataFrame:
    """
    Describe the content of a csv & apply functions to his rows:
     - total count & count
     - mean
     - std
     - min
     - quantile (25%, 50%, 75%)
     - max

    Args:
        values    (DataFrame): DataFrame of the parsed csv to compute

    Returns:
        DataFrame: newly created DataFrame
    """
    numeric = data.select_dtypes(include='number')
    numeric = numeric.drop(columns=['Index'], errors='ignore')

    stats = {
        'total count': {col: ft_count(numeric[col].values)
                        for col in numeric.columns},
        'count': {col: ft_count(numeric[col].dropna().values)
                  for col in numeric.columns},
        'mean':  {col: ft_mean(numeric[col].dropna().values)
                  for col in numeric.columns},
        'std':   {col: ft_std(numeric[col].dropna().values)
                  for col in numeric.columns},
        'min':   {col: ft_min(numeric[col].dropna().values)
                  for col in numeric.columns},
        '25%':   {col: ft_quantile(numeric[col].dropna().values, 0.25)
                  for col in numeric.columns},
        '50%':   {col: ft_quantile(numeric[col].dropna().values, 0.50)
                  for col in numeric.columns},
        '75%':   {col: ft_quantile(numeric[col].dropna().values, 0.75)
                  for col in numeric.columns},
        'max':   {col: ft_max(numeric[col].dropna().values)
                  for col in numeric.columns},
    }

    result = DataFrame(stats).T
    print(result)
    return (result)


def main():
    if len(sys.argv) != 2:
        print("Usage: ./describe.py <file.csv>")
        return (1)
    try:
        data: DataFrame = read_csv(sys.argv[1])
        describe(data)
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
