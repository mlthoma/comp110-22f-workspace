"""Making 'list' utility functions."""
__author__ = "730578788"


def all(integer_list: list[int], integer: int) -> bool:
    """Determines whether or not all of the ints in the integer_list are equal to the given integer."""
    i: int = 0
    if len(integer_list) == 0:
        return False
    while i < len(integer_list):
        if integer_list[i] != integer:
            return False
        i += 1
    
    return True


def max(list_input: list[int]) -> int:
    """Returns the maximum value out of the ints in the list."""
    i: int = 0
    if len(list_input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        maximum: int = list_input[0]
        while i < len(list_input):
            if list_input[i] > maximum:
                maximum = list_input[i]
            i += 1
        return maximum


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Determines whether or not all of the elements in all of the indexes are equal in both lists."""
    i: int = 0
    if len(list1) == 0 and len(list2) == 0:
        return True
    elif len(list1) == 0 or len(list2) == 0 or len(list1) != len(list2):
        return False
    while i < len(list1) or i < len(list2):
        if list1[i] != list2[i]:
            return False
        i += 1
    return True
        
