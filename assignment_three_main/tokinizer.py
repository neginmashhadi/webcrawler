'''
This file is part A of assigment one for CS 121.

This file has been modified to now work with assignment 3.
The core idea behind this file is still the same with slight
modifications.
'''


import re

from nltk.stem import PorterStemmer


def main_tokinizer(html_content: str) -> {}:
    '''
    This is the main function. Takes in html content, tokinizes the content
    and then returns a dictionary with the token as a key and the frequency
    as the value.
    '''
    token_dict = tokinize_content(html_content)

    return list(token_dict.keys())


def tokinize_content(html_content: str) -> {}:
    '''
    Takes in html content and tokinizes. Returns a dictionary of the words
    tokinized and their frequencies.
    '''
    tokinized_dict = {}

    _tokinize_line(html_content, tokinized_dict)

    return tokinized_dict


def _tokinize_line(current_line: str, tokinized_dict: {}) -> None:
    '''
    Takes in a string and a dict that is either empty or has keys and values
    representing the tokens. Splits the line by alphanumeric strings, stems
    them using porter stemming and then puts them inside the dictionary.
    Returns nothing.
    '''
    pattern = [r'[a-zA-Z0-9]+']

    tokens_list = re.findall(pattern[0], current_line)
    ps = PorterStemmer()

    for string in tokens_list:
        stemed_string = ps.stem(string)

        if stemed_string not in tokinized_dict:
            tokinized_dict[stemed_string] = None
