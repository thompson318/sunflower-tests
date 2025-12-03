import sunflower.fibonacci
import pytest


def test_fib_0_returns_0():
    # ARRANGE

    # ACT
    res = sunflower.fibonacci.fibonacci(0)

    # ASSERT
    assert res == 0


def test_fib_neg_1_fails():
    # ARRANGE

    # ACT

    # ASSERT
    with pytest.raises(ValueError, match="Fibonacci has a natural number domain."):
        sunflower.fibonacci.fibonacci(-1)


expected_fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

@pytest.mark.parametrize("rank, expected", enumerate(expected_fib))
def test_valid_fib_input(rank, expected):
    # ARRANGE

    # ACT
    res = sunflower.fibonacci.fibonacci(rank)

    # ASSERT
    assert res == expected
