import re
from collections import defaultdict
import sys


def find_anagrams(word_list):

    word_hash = defaultdict(list)

    for word in word_list:
        key = tuple(sorted(list(word)))
        if word not in word_hash[key]:
            word_hash[key].append(word)

    return [x for x in list(word_hash.values()) if len(x)>1]


def clean_english(a_string):

    a_string = a_string.lower().replace('\n', ' ')

    a_string = re.sub(r"['|’][a-zA-Z](?= )", " ", a_string)

    a_string = re.sub(r'[^a-zA-Z ]', ' ', a_string)

    return a_string


if __name__ == '__main__':

    text_file = sys.argv[1]

    with open(text_file, 'r') as a_text_file:
        data = a_text_file.read()

    data = clean_english(data)

    data = data.split()

    print(find_anagrams(data))
