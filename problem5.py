"""
Problem 5 (30): Write a program (C++, C#, Java, Python) that parses a file and for each string it finds
(strings are separated by whitespace) outputs the string and which of the above languages it is a member of.
If the string is not a member of any, then it outputs 'none'. For organizational reasons, make a boolean
function for each of the languages. Please provide appropriate and helpful comments.

Example Run:

    File: test.txt
    Abcde: Id
    aAa9: Id
    3422222: Num
    ;: Semicolon
    wHile: Id
    while: Id, While
    &&: And
    8eo: none
    &: none
    ;asdf: none

"""

from p5_dfa_definitions import *
from p5_dfa_testing import *

# reads file, splits into array
def split_readfile():
    with open("test.txt") as file:
        open_line = file.readline()
        lines = open_line.split()
    return lines

# logic to print out accepting DFAs in file
def whichDFA():
    lines = split_readfile()
    print("File: test.txt")
    for x in lines:
        all_reject = True # variable to print none AND inset commas where needed
        print(x + ": ", end='')  # prints line name
        if id_A.accepts_input(x): # if True, print Id
            print("Id", end='')
            all_reject = False # flag variable flip
        if num_B.accepts_input(x):
            if all_reject == False:
                print(", ", end='')
            print("Num", end='')
            all_reject = False
        if semicolon_C.accepts_input(x):
            if all_reject == False:
                print(", ", end='')
            print("Semicolon", end='')
            all_reject = False
        if and_D.accepts_input(x):
            if all_reject == False:
                print(", ", end='')
            print("And", end='')
            all_reject = False
        if while_E.accepts_input(x):
            if all_reject == False:
                print(", ", end='')
            print("While", end='')
            all_reject = False
        if all_reject == True:
            print("none", end='')
        print("")
whichDFA()
