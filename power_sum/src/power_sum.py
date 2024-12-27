"""
Given a number x and a power n, we  need to find the number of ways that x can be
represented as the sum of unique numbers elevated to the power of n.

Constraints:
1 < x < 1000
2 < n < 10
"""


def power_sum(x: int, n: int, current_num: int = 1):
    current_power = current_num**n
    # base cases
    if x == 0:
        return 1
    if x < 0 or current_power > x:
        return 0

    include_path = power_sum(x=x - current_power, n=n, current_num=current_num + 1)
    exclude_path = power_sum(x=x, n=n, current_num=current_num + 1)

    return include_path + exclude_path
