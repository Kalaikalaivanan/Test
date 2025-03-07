import pytest

def test_total_divisible_by_10(input_total):
    assert input_total % 10 == 0


def test_total_divisible_by_20(input_total):
    assert input_total % 20 == 0
