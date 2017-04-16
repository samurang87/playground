def powerset(a_list):

    if not a_list:
        yield []

    else:
        head, tail = a_list[:1], a_list[1:]

        for i in powerset(tail):
            yield i
            yield head + i


if __name__ == '__main__':

    print(list(powerset([1, 2, 3, 4])))
