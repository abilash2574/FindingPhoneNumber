#! python3
# phonenumber.py - This script finds all the phone number that are present in an text.
# Standard Indian phone number goes as "+91-AAAAA BBBBB" where the +91- can be omitted.

import pyperclip


def isphonenumber(number):
    if len(number) != 11:
        return False
    for i in range(5):
        if not number[i].isdecimal():
            return False
    if number[5] != ' ':
        return False
    for i in range(6,11):
        if not number[i].isdecimal():
            return False
    return True

print(isphonenumber("98433 37331"))
