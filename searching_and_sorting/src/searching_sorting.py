from typing import Any, List


def mergesort(input: List[Any], left_i: int, right_i: int) -> List[Any]:
    if left_i >= right_i:
        return
    mid = (left_i + right_i) // 2
    mergesort(input, left_i, mid)
    mergesort(input, mid + 1, right_i)
    merge(input, left_i, right_i, mid)


def merge(input: List[Any], left_i: int, right_i: int, mid: int) -> List[Any]:
    print(input)
    left = input[left_i:mid + 1]
    right = input[mid + 1 : right_i + 1]

    left_copy_i = 0
    right_copy_i = 0
    sorted_index = left_i

    while left_copy_i < len(left) and right_copy_i < len(right):
        if left[left_copy_i] < right[right_copy_i]:
            input[sorted_index] = left[left_copy_i]
            left_copy_i += 1
        else:
            input[sorted_index] = right[right_copy_i]
            right_copy_i += 1
        sorted_index += 1

    while left_copy_i < len(left):
        input[sorted_index] = left[left_copy_i]
        left_copy_i += 1
        sorted_index += 1

    while right_copy_i < len(right):
        input[sorted_index] = right[right_copy_i]
        right_copy_i += 1
        sorted_index += 1


def sorted_merge(a: List[int], b: List[int]) -> List[int]:
    """
    10.1
    """
    count_iter = 0
    max_index = 0
    for item_b in b:
        if max_index >= len(a) - 1:
            a.extend(b[b.index(item_b) :])
            count_iter += 1
            return a
        for item_a in a[max_index:]:
            count_iter += 1
            if item_b <= item_a:
                a.insert(a.index(item_a), item_b)
                max_index = a.index(item_a)
                break
    print(count_iter)
    return a

if __name__ == "__main__":

    input = [3, 1]

    mergesort(input, 0, len(input)-1)

    print(input)