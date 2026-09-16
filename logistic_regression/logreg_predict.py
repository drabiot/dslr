#!/usr/bin/env -S uv run --script

import sys
sys.path.append("..")
sys.path.append(".")
sys.path.append("./logistic_regression")

from pandas import read_csv, DataFrame, Series  # noqa: E402
from math import exp, log
from pandas.errors import EmptyDataError, ParserError  # noqa: E402

def predict(data: DataFrame):
    target_col = "Hogwarts House"
    feature = ["Herbology","Defense Against the Dark Arts","Divination","Ancient Runes","History of Magic"]
    cols_to_keep = feature + [target_col]
    clean_data = data[cols_to_keep].dropna().copy()

    X = clean_data[feature]
    y_raw = clean_data[target_col]

    X = (X - X.mean()) / X.std()
    X.insert(0, 'Intercept', 1.0)

    alpha = 0.1
    iterations = 1000

    classes = y_raw.unique()
    all_thetas = {}

    for cls in classes:
        y_binary = (y_raw == cls).astype(int)
        theta_initial = Series(0.0, index = X.columns)

        optimal_theta = gradient_descent(X, y_binary, theta_initial, alpha, iterations)
        all_thetas[cls] = optimal_theta


    weights_df = DataFrame(all_thetas)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"weights_{timestamp}.csv"

    weights_df.to_csv(filename)

def main():
    if len(sys.argv) != 3:
        print("Usage: ./describe.py <file.csv> <weight.csv>")
        return (1)
    try:
        data: DataFrame = read_csv(sys.argv[1])
        predict(data)
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