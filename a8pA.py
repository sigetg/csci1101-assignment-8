# Write a program to convert songs from the Latin note convention to the
# Anglo-saxon note convention.  Specifically, in Latin, the 7 music notes are
# "do", "re", "mi", "fa", "sol", "la", "si", and their equivalents in
# Anglo-saxon are "C", "D", "E", "F", "G", "A", "B".  Create a dictionary to
# store the translations.  Then, the user will enter Latin notes, each on their
# own line.  When the user enters any value that isn't one of the Latin notes,
# stop reading inputs and print out the translated notes in Anglo-saxon.
# The translated notes should be all on one line separated by spaces.
#
# You are required to create at least 3 functions to solve this problem:
#
# 1) A function named get_latin_notes(), with no parameters, that prompts the
#    user to enter Latin notes, each on their own line. The function must return
#    the latin notes in a list. Stop adding values to the list and return when
#    you read any value that is not one of the 7 Latin note names.  String case
#    should be insensitive, i.e., "DO", "do", "Do", and "dO" are all the same.
# 2) A function named latin_to_anglosaxon(), that takes a single parameter.
#    The parameter is a list of Latin notes.  The function must return a new
#    list with the same notes but translated to the Anglo-Saxon convention.
#    You must use a dictionary to do this translation.
# 3) A function named print_list() that takes a single list as a parameter and
#    prints every element in that list on the same line.  The function must put
#    a single space after each element and print a new line once all elements
#    have been printed.
#
# You must create a dictionary with the translations from Latin to Anglo-Saxon
# note names.  This dictionary won't change, and so should be considered a
# "constant" variable.  Follow all conventions for such constants.  That means
# that you should create the dictionary above the function definitions in the
# python file, use it in your functions as a global constant, and be sure to
# name the dictionary in all caps.
#
# Your input and output messages must conform to the following examples:
#
# Enter Latin notes each on their own line:
# done
# No notes entered!
#
# Enter Latin notes each on their own line:
# Do
# RE
# mi
# quit
# The notes in Anglo-Saxon:
# C D E
#
# Enter Latin notes each on their own line:
# mi
# mi
# mi
# mi
# re
# do
# re
# mi
# fa
# sol
# sol
# sol
# fin
# The notes in Anglo-Saxon:
# E E E E D C D E F G G G
#
# Note the order of inputs, capitalization of messages, spacing, etc.

import sys

def get_latin_notes():
    user_latin_notes = []
    latin_notes = ["do", "re", "mi", "fa", "sol", "la", "si"]
    value = "do"
    print("Enter Latin notes each on their own line:")
    while value in latin_notes:
        value = input()
        value = value.lower()
        if value in latin_notes:
            user_latin_notes.append(value)
    if user_latin_notes == []:
        print("No notes entered!", "\n")
        sys.exit()
    return user_latin_notes

def latin_to_anglosaxon(user_latin_notes):
    translated_notes = []
    translations = {"do":"C", "re":"D", "mi":"E", "fa":"F", "sol":"G", "la":"A", "si":"B"}
    for note in user_latin_notes:
        translated_notes.append(translations[note])
    return translated_notes

def print_list(some_list):
    for value in some_list:
        print(value, end=" ")
    print("\n")

user_latin_notes = get_latin_notes()
translated_notes = latin_to_anglosaxon(user_latin_notes)
print("The notes in Anglo-Saxon:")
print_list(translated_notes)
























