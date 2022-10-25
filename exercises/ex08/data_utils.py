"""Dictionary related utility functions."""

__author__ = "730578788"

# Define your functions below
from csv import DictReader


def read_csv_rows(csv_path: str) -> list[dict[str, str]]:
    """Reads a CSV data file into a list of rows. Each row is represented as dict[str, str]."""
    rows: list[dict[str, str]] = []
    file_handle = open(csv_path, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for line in csv_reader:
        rows.append(line)
    file_handle.close()
    return rows


def column_values(table: list[dict[str, str]], key: str) -> list[str]:
    """Produces a list of all values in a single column (key)."""
    column_values_list: list[str] = []
    for dictionary in table:
        column_values_list.append(dictionary[key])
    return column_values_list


def columnar(list_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a table represented as a list of rows into one represented as a dictionary of columns."""
    column_dictionary: dict[str, list[str]] = {}
    for row in list_table:
        for column_name in row:
            if column_name in column_dictionary:
                column_dictionary[column_name].append(row[column_name])
            else:
                column_dictionary[column_name] = [row[column_name]]
    return column_dictionary


def head(column_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first parameter number of rows of data for each column."""
    dictionary: dict[str, list[str]] = {}
    for columns in column_table:
        first_n_values_list: list[str] = []
        i: int = 0
        if rows > len(column_table):
            return column_table
        while i < rows:
            first_n_values_list.append(column_table[columns][i])
            i += 1
        dictionary[columns] = first_n_values_list
    return dictionary


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only a specific subset of the original columns."""
    returned_dictionary: dict[str, list[str]] = {}
    for columns in column_names:
        returned_dictionary[columns] = column_table[columns]
    return returned_dictionary


def concat(column_table_1: dict[str, list[str]], column_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-based table with 2 column-based tables combined."""
    dictionary: dict[str, list[str]] = {}
    for columns in column_table_1:
        dictionary[columns] = column_table_1[columns]
    for columns in column_table_2:
        if columns in dictionary:
            dictionary[columns] = dictionary[columns] + column_table_2[columns]
        else:
            dictionary[columns] = column_table_2[columns]
    return dictionary


def count(values: list[str]) -> dict[str, int]:
    """Produces a dictionary where each key is a unique value in the given list and each value is the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
