import string
import sys
from collections import Counter

file = sys.argv[1]

def read_file(file):
    with open(file, 'r') as read_file:
        words = []
        for line in read_file:
            line = line.rstrip().split(' ')
            for word in line:
                if word[-1] in string.punctuation:
                    word = word[:-1]
                word = word.lower()
                words.append(word)
    return words

def wordcount(ls):
    word_dict = {}

    for word in ls:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

    # for key, value in word_dict.items():
    #     print(f'{key} {value}')


read_lines = read_file(file)
print(sorted(wordcount(read_lines).items(), key=wordcount(read_lines).values()))

# use collections.Counter in code below

def word_counter(file):
    f = open(file, 'r')
    read_file = f.read().split(' ')
    return Counter(read_file)

# print(word_counter(file))