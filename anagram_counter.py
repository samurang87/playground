from collections import defaultdict

def find_anagrams(word_list):

    word_hash = defaultdict(list)

    for word in word_list:
        word_hash[frozenset(list(word))].append(word)

    return sorted(list(word_hash.values()))
