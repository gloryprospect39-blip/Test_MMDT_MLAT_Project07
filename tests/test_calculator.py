import pytest

from src.calculator import (
    calculate_average,
    factorial,
    find_maximum,
    is_prime,
    power,
)


@pytest.mark.parametrize(
    "scores, expected",
    [
        ([90, 80, 70], 80.0),
        ((70, 80, 90), 80.0),
        ([100, 0, 50], 50.0),
        ([10, 20, 30, 40], 25.0),
    ],
)
def test_calculate_average_valid_scores(scores, expected):
    assert calculate_average(scores) == expected


def test_calculate_average_rejects_empty_list():
    with pytest.raises(ValueError, match="empty"):
        calculate_average([])


def test_calculate_average_rejects_invalid_types():
    with pytest.raises(TypeError):
        calculate_average("not a list")

    with pytest.raises(TypeError):
        calculate_average([90, "a", 80])

    with pytest.raises(TypeError):
        calculate_average([90, True, 80])


@pytest.mark.parametrize(
    "scores, expected",
    [
        ([5, 1, 9, 3], 9),
        ((-3, -10, -7), -3),
        ([42], 42),
        ([0.5, 2.5, -1.0], 2.5),
    ],
)
def test_find_maximum_valid_scores(scores, expected):
    assert find_maximum(scores) == expected


def test_find_maximum_rejects_invalid_values():
    with pytest.raises(ValueError, match="empty"):
        find_maximum([])

    with pytest.raises(TypeError):
        find_maximum([1, "two", 3])


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (17, True),
        (49, False),
        (97, True),
    ],
)
def test_is_prime(value, expected):
    assert is_prime(value) is expected


def test_is_prime_rejects_invalid_input_types():
    with pytest.raises(TypeError):
        is_prime(2.5)

    with pytest.raises(TypeError):
        is_prime(True)


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 1),
        (1, 1),
        (5, 120),
        (7, 5040),
    ],
)
def test_factorial(value, expected):
    assert factorial(value) == expected


def test_factorial_rejects_invalid_inputs():
    with pytest.raises(TypeError):
        factorial(3.5)

    with pytest.raises(TypeError):
        factorial(True)

    with pytest.raises(ValueError):
        factorial(-1)


@pytest.mark.parametrize(
    "base, exponent, expected",
    [
        (2, 3, 8),
        (3.0, 2, 9.0),
        (2.5, 2, 6.25),
        (10, 0, 1),
    ],
)
def test_power_valid_cases(base, exponent, expected):
    assert power(base, exponent) == expected


def test_power_rejects_invalid_inputs():
    with pytest.raises(TypeError):
        power("2", 3)

    with pytest.raises(TypeError):
        power(2, 2.0)

    with pytest.raises(TypeError):
        power(True, 2)

    with pytest.raises(ValueError):
        power(0, -1)
