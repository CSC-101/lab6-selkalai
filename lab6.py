from os import close

import data
from typing import Optional
from data import Book
import math


# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp

# Part 1
#function selection_sort_books will take one parameter of type
# list[Book(self, authors: list[str], title: str). The function will modify the
#provided selection sort function to sort the list of book alphabetically by title.

def closest_to_a(books:list[Book], start:int) -> Optional[int]:
    if start >= len(books) or start < 0:
        return None

    min_idx = start
    for idx in range(start + 1, len(books)):
        if books[idx].title[0] < books[min_idx].title[0]:
            min_idx = idx

    return min_idx

def selection_sort_books(books:list[Book])->list:

    for idx in range(len(books)-1):
        min_idx = closest_to_a(books, idx)
        tmp = books[min_idx]
        books[min_idx] = books[idx]
        books[idx] = tmp
    return_list = []
    for i in books:
        return_list.append(i.title)
    return return_list


# Part 2
#function swap_case takes one parameter of type str and returns a str. the return will swap the
# cases of the characters in the string. all other characters stay unmodified between the
# input string and the result.

def swap_case(phrase:str)->str:
    phrase_list = []

    for char in phrase:
        if char.islower():
            phrase_list.append(char.upper())
        elif char.isupper():
            phrase_list.append(char.lower())
        else:
            phrase_list.append(char)
    return "".join(phrase_list)

# Part 3
#function str_translate takes three parameters: a string (of type str) and two characters
# (old and new; one character strings). The function will return a new string where
# each occurrence of old in the input string is replaced with new (and all other characters
# are left unchanged).

def str_translate(phrase:str, old:str, new:str)->str:
    new_phrase = []
    for char in phrase:
        if char == old:
            new_phrase.append(new)
        else:
            new_phrase.append(char)
    return "".join(new_phrase)

# Part 4
#function histogram takes a single string and returns a dictionary mapping strings to
# integers. This function must return a dictionary that maps each "word" from the
# input string to a count of the number of times that word appears in the string.

def histogram(paragraph:str)->dict:
    new_dict = {}
    words = paragraph.split()

    for word in words:
        if word in words:
            if word in new_dict:
                new_dict[word] += 1
            else:
                new_dict[word] = 1
    return new_dict





