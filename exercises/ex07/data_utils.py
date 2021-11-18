"""Utility functions."""

__author__ = "730316359"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read data from a stored CSV file into memory."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column whose name is the second parameter."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows into a dictionary of columns."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_based_table: dict[str, list[str]], number_of_rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table."""
    result: dict[str, list[str]] = {}
    for column in column_based_table:
        list_of_values: list[str] = []
        i = 0
        if number_of_rows > len(column_based_table):
            result = column_based_table
        else:
            while i < number_of_rows:
                list_of_values.append(column_based_table[column][i])
                i += 1
            result[column] = list_of_values
    return result


def select(column_based_table: dict[str, list[str]], name: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in name:
        result[column] = column_based_table[column]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in table_1:
        result[column] = table_1[column]
    for column in table_2:
        if column in table_1:
            result[column] += table_1[column]
        else:
            result[column] = table_2[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Produce a dictionary where each key is a unique value and each value is associated with count."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result