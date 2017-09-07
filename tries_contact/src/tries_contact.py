import sys


def add_word(trie, word):

    if word[0] not in trie:

        trie[word[0]] = dict()

    if len(word) > 1:

        add_word(trie[word[0]], word[1:])

    else:

        trie[word[0]]["*"] = None


def found_partial():

    found_partial.counter += 1


def count_leaves(partial_trie):

    if '*' in partial_trie:

        found_partial()

    for char in partial_trie:

        if char != '*':

            count_leaves(partial_trie[char])


def find_partial(trie, word):

    if word[0] in trie:

        if len(word) > 1:

            find_partial(trie[word[0]], word[1:])

        else:

            count_leaves(trie[word[0]])


if __name__ == "__main__":

    trie = dict()

    for linenum, line in enumerate(sys.stdin):

        if linenum != 0:

            instruction = line.split(" ")

            if instruction[0] == "add":

                add_word(trie, instruction[1].rstrip())

            elif instruction[0] == "find":

                found_partial.counter = 0

                try:

                    find_partial(trie, instruction[1].rstrip())

                    print(found_partial.counter)

                except KeyError:

                    print('KeyError in {}'.format(instruction[1]))

            else:

                raise ValueError('Invalid command!')
