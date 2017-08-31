from itertools import chain
import sys

"""
Quicksort exercise from Hackerrank
"""


def partition(unsorted: list):

    left, mid, right = [], [], []

    pivot = unsorted[0]

    for number in unsorted:

        if number < pivot:
            left.append(number)

        elif number > pivot:
            right.append(number)

        else:
            mid.append(number)

    return left, mid, right


def merge(collections: list):

    #for position, collection in enumerate(collections):

    #     if len(collection) > 1 and position % 2 == 0:
    #         print(" ".join(str(item) for item in collection))
    #
    # return list(chain(*collections))

    merged = list(chain(*collections))

    print(" ".join(str(item) for item in merged))

    return merged

def quicksort(unsorted: list):

    if len(unsorted) <= 1:

        return unsorted

    else:
        left, mid, right = partition(unsorted)

        return merge([quicksort(left), mid, quicksort(right)])


if __name__ == "__main__":

    input = []

    for line in sys.stdin:

        input.append([int(n) for n in str.split(line)])

    for i, array in enumerate(input):

        if i % 2 != 0:

            print(" ".join(str(item) for item in quicksort(array)))
