import pytest

from power_sum.src.power_sum import power_sum


@pytest.mark.parametrize(
    "x,n,result",
    [
        (13, 2, 1),
        (100, 2, 3),
    ],
)
def test_power_sum(x: int, n: int, result: int):
    assert power_sum(x, n) == result
