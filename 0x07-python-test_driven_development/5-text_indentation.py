#!/usr/bin/python3
"""
module for text_indentation function implementation
"""


def text_indentation(text):
    # check if the input is a string
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    #  printtext with 2 new lines after each of these characters: ., ? and :

    for delim in ".?:":
        # print(delim, text.split(delim))
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
