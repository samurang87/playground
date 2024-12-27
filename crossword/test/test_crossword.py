import pytest

from crossword.src.crossword import (
    crossword_wrapped,
    fits,
    make_new_row_col,
    prep_input,
)


@pytest.mark.parametrize(
    "original, insert, index, result",
    [("----+", "casa", 0, "casa+"), ("++----++", "casa", 2, "++casa++")],
)
def test_make_row(original, insert, index, result):
    assert make_new_row_col(insert, original, index) == result


@pytest.mark.parametrize(
    "original, insert, index, result",
    [
        ("----+", "casa", 0, True),
        ("++-a--++", "casa", 2, True),
        ("--", "casa", 0, False),
        ("++------", "casa", 2, False),
        ("++++---", "casa", 2, False),
        ("+++---b", "casa", 2, False),
        ("++a----", "casa", 2, False),
    ],
)
def test_fits(original, insert, index, result):
    assert fits(insert, original, index) is result


def test_prep_input():
    input = """
+-++++++++
+-++++++++
+-++++++++
+-----++++
+-+++-++++
+-+++-++++
+++++-++++
++------++
+++++-++++
+++++-++++
LONDON;DELHI;ICELAND;ANKARA
"""

    output = (
        [
            "+-++++++++",
            "+-++++++++",
            "+-++++++++",
            "+-----++++",
            "+-+++-++++",
            "+-+++-++++",
            "+++++-++++",
            "++------++",
            "+++++-++++",
            "+++++-++++",
        ],
        ["LONDON", "DELHI", "ICELAND", "ANKARA"],
    )

    assert prep_input(input) == output


def test_crossword_sample_0():
    input = """+-++++++++
+-++++++++
+-++++++++
+-----++++
+-+++-++++
+-+++-++++
+++++-++++
++------++
+++++-++++
+++++-++++
LONDON;DELHI;ICELAND;ANKARA"""

    output = """+L++++++++
+O++++++++
+N++++++++
+DELHI++++
+O+++C++++
+N+++E++++
+++++L++++
++ANKARA++
+++++N++++
+++++D++++"""

    assert crossword_wrapped(input) == output


def test_crossword_sample_1():
    input = """+-++++++++
+-++++++++
+-------++
+-++++++++
+-++++++++
+------+++
+-+++-++++
+++++-++++
+++++-++++
++++++++++
AGRA;NORWAY;ENGLAND;GWALIOR"""

    output = """+E++++++++
+N++++++++
+GWALIOR++
+L++++++++
+A++++++++
+NORWAY+++
+D+++G++++
+++++R++++
+++++A++++
++++++++++"""

    assert crossword_wrapped(input) == output


def test_crossword_sample_6():
    input = """+-++++++++
+-------++
+-++-+++++
+-------++
+-++-++++-
+-++-++++-
+-++------
+++++++++-
++++++++++
++++++++++
ANDAMAN;MANIPUR;ICELAND;ALLEPY;YANGON;PUNE"""

    output = """+M++++++++
+ANDAMAN++
+N++L+++++
+ICELAND++
+P++E++++P
+U++P++++U
+R++YANGON
+++++++++E
++++++++++
++++++++++"""

    assert crossword_wrapped(input) == output
