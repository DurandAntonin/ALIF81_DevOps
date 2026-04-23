import math
import pytest

from src.services.calculatrice_service import add, mult, reduce, divide


class TestService:
    def test_add_success(self):
        x, y = 2, 3
        assert 5 == add(x, y)

    def test_mult_success(self):
        x, y = 2, 3
        assert 6 == mult(x, y)

    def test_reduce_success(self):
        x, y = 2, 3
        assert -1 == reduce(x, y)

    def test_divide_success(self):
        x, y = 1, 2
        assert math.isclose(0.5, divide(x, y), rel_tol=1e-09, abs_tol=1e-09)

    def test_divide_with_0_as_second_argument(self):
        x, y = 5, 0
        with pytest.raises(ZeroDivisionError):
            divide(x, y)