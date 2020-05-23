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


text = "Hey this is my number note it, 98433 37331. make sure you call me, see you later"

for i in range(len(text)):
    chunk = text[i:i+11]
    if isphonenumber(chunk):
        print("The phone number is "+ chunk)
        break
    else:
        print("Phone number can't be found")
