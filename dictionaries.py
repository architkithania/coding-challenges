# Problem 22
from sys import getsizeof
def dictionary_creator(words):
    word_dict = {}
    for word in words:
        dict_at_work = word_dict
        for i, char in enumerate(word):
            if char in dict_at_work:
                dict_at_work = dict_at_work[char]
            else:
                if i == len(word) - 1:
                    dict_at_work[char] = {'#': word}
                else:
                    dict_at_work[char] = {}
                    dict_at_work = dict_at_work[char]
    return word_dict

def word_list_creator(word_str, words):
    word_dict = dictionary_creator(words)
    print(getsizeof(word_dict))
    dict_at_work = word_dict
    word_list = []
    for i, char in enumerate(word_str):
        dict_at_work = dict_at_work[char]
        if '#' in dict_at_work:
            if len(dict_at_work) == 1 or i == len(word_str) - 1 or word_str[i+1] not in dict_at_work:
                word_list.append(dict_at_work['#'])
                dict_at_work = word_dict
    return word_list

print(word_list_creator("bedbathandbeyond", ['bed', 'bedbath', 'and', 'beyond']))