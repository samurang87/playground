from collections import OrderedDict


class WrongOrderException(Exception):
    pass


val_list = [('M', 1000),
            ('D', 500),
            ('C', 100),
            ('L', 50),
            ('X', 10),
            ('V', 5),
            ('I', 1),
            ('O', 0),
            ]

allowed_subtractions = {'I': ('V', 'X'),
                        'X': ('L', 'C'),
                        'C': ('D', 'M')}

VALS = OrderedDict(val_list)


def _check_roman(roman_string):

    for pos in range(len(roman_string) - 1):

        try:

            if len(roman_string[pos:]) > 2:

                if VALS[roman_string[pos]] == VALS[roman_string[pos + 1]] \
                        and VALS[roman_string[pos]] < VALS[roman_string[pos + 2]]:

                    raise WrongOrderException

            if VALS[roman_string[pos]] < VALS[roman_string[pos +1]] \
                    and roman_string[pos+1] not in allowed_subtractions[roman_string[pos]]:

                raise WrongOrderException

        except KeyError:

                raise WrongOrderException


def roman_to_int(roman_string):

    _check_roman(roman_string)

    sum_roman = 0

    while len(roman_string) > 1:

        if VALS[roman_string[0]] < VALS[roman_string[1]]:

            sum_roman -= VALS[roman_string[0]]

        else:

            sum_roman += VALS[roman_string[0]]

        roman_string = roman_string[1:]

    sum_roman += VALS[roman_string]

    return sum_roman

