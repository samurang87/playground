def add_word(trie, word):

    trie.setdefault(word[0], dict())

    if len(word) > 1:

        add_word(trie[word[0]], word[1:])

    else:

        trie[word[0]]["*"] = None


def found_partial():

    found_partial.counter += 1


def count_leaves(partial_trie):

    for char in partial_trie:

        if char != '*':

            count_leaves(partial_trie[char])

        else:
            found_partial()


def find_partial(trie, word):

    if word[0] in trie:

        if len(word) > 1:

            find_partial(trie[word[0]], word[1:])

        else:

            count_leaves(trie[word[0]])


if __name__ == "__main__":

    trie = dict()

    n = int(input().strip())

    for a0 in range(n):

        instruction, word = input().strip().split(' ')

        if instruction == "add":

            add_word(trie, word)

        elif instruction == "find":

            found_partial.counter = 0

            find_partial(trie, word)

            print(found_partial.counter)

        else:

            raise ValueError('Invalid command!')
