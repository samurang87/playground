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


if __name__ == '__main__':

    text_file = sys.argv[1]

    with open(text_file, 'r') as a_text_file:
        data = a_text_file.read()

    data = data.lower().replace('\n', ' ')

    data = data.replace("’s", "")

    data = re.sub(r"['|’][a-zA-Z](?= )", "", data)

    data = re.sub(r'[^a-zA-Z ]', '', data)

    data = data.split()

    print(find_anagrams(data))
