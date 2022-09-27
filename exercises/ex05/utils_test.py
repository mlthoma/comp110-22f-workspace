"""Building unit tests for the function skeletons."""
__author__ = "730578788"

from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Tests edge case for empty list."""
    numbers: list[int] = []
    assert only_evens(numbers) == []


def test_only_evens_same_numbers() -> None:
    """Tests used case for a list of duplicate integers."""
    numbers: list[int] = [6, 6, 6]
    assert only_evens(numbers) == [6, 6, 6]


def test_only_evens_varying_numbers() -> None:
    """Tests used case for a list of different integers."""
    numbers: list[int] = [6, 7, 8, 4]
    assert only_evens(numbers) == [6, 8, 4]


def test_concat_empty() -> None:
    """Tests edge case for two empty lists."""
    numbers_1: list[int] = []
    numbers_2: list[int] = []
    assert concat(numbers_1, numbers_2) == []


def test_concat_same_numbers() -> None:
    """Tests used case for lists of duplicate integers."""
    numbers_1: list[int] = [7, 7, 7, 7]
    numbers_2: list[int] = [7, 7, 7]
    assert concat(numbers_1, numbers_2) == [7, 7, 7, 7, 7, 7, 7]


def test_concat_varying_numbers() -> None:
    """Tests used case for lists of varying numbers."""
    numbers_1: list[int] = [2, 3, 4]
    numbers_2: list[int] = [5, 6, 7]
    assert concat(numbers_1, numbers_2) == [2, 3, 4, 5, 6, 7]


def test_sub_negative_start() -> None:
    """Tests edge case when the start index is negative."""
    numbers_list: list[int] = [2, 3, 4, 5]
    number_1: int = -1
    number_2: int = 3
    assert sub(numbers_list, number_1, number_2) == [2, 3, 4]


def test_sub_varying_numbers_expected_indices() -> None:
    """Tests used case for a list of varying integers and expected start and end indices."""
    numbers_list: list[int] = [3, 5, 4, 6, 8]
    number_1: int = 1
    number_2: int = 4
    assert sub(numbers_list, number_1, number_2) == [5, 4, 6]


def test_sub_same_numbers_expected_indices() -> None:
    """Tests used case for a list of duplicated numbers with the expected start and end indices."""
    numbers_list: list[int] = [1, 1, 1, 1, 1]
    number_1: int = 0
    number_2: int = 3
    assert sub(numbers_list, number_1, number_2) == [1, 1, 1]
