"""Building list utility functions with unit tests. Implements function skeletons and implementations."""
__author__ = "730578788"


def only_evens(integer_list: list[int]) -> list[int]:
    """Returns even elements of the input list."""
    i: int = 0
    even_list: list[int] = []
    while i < len(integer_list):
        if integer_list[i] % 2 == 0:
            even_list.append(integer_list[i])
        i += 1
    return even_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Returns list containing all of the elements of the first list, followed by elements of the second list."""
    concat_list: list[int] = []
    i: int = 0
    while i < len(list_1):
        concat_list.append(list_1[i])
        i += 1
    i = 0
    while i < len(list_2):
        concat_list.append(list_2[i])
        i += 1
    return concat_list


def sub(integer_list: list[int], integer_1: int, integer_2: int) -> list[int]:
    """Returns a subset list of the given list between the specified start and end indices."""
    i: int = integer_1
    sub_list: list[int] = []
    if integer_1 < 0:
        i = 0
    elif integer_2 > len(integer_list):
        integer_2 = len(integer_list)
    elif len(integer_list) == 0 or integer_1 > len(integer_list) or integer_2 == 0:
        return sub_list
    while i < integer_2:
        sub_list.append(integer_list[i])
        i += 1
    return sub_list