import unittest

from tries_contact.src.tries_contact import add_word, count_leaves, found_partial, find_partial


class TestTries(unittest.TestCase):

    def test_single_word_add(self):

        trie = dict()

        add_word(trie, "bla")

        expected = {'b': {'l': {'a': {'*': None}}}}

        self.assertDictEqual(trie, expected)

    def test_add_more_words(self):

        trie = dict()

        add_word(trie, "bla")

        add_word(trie, "blub")

        expected = {'b': {'l': {'a': {'*': None},
                                'u': {'b': {'*': None}}}}}

        self.assertDictEqual(trie, expected)

    def test_count_leaves(self):

        trie = {'a': {'*': None},
                'u': {'b': {'*': None}}}

        found_partial.counter = 0

        count_leaves(trie)

        self.assertEqual(found_partial.counter, 2)

    def test_find_partial(self):

        trie = {'b': {'l': {'a': {'*': None},
                            'u': {'b': {'*': None}}}}}

        found_partial.counter = 0

        find_partial(trie, 'bl')

        self.assertEqual(found_partial.counter, 2)
