#! python3
# Creating the same program using re package

import re

indian_pattern = re.compile(r'\d\d\d\d\d \d\d\d\d\d')
text = "This is my number 76833 12142."
search = indian_pattern.search(text)
val = lambda x: None if(search==None) else search.group()
if val(search) != None:
    print ("The phone number is "+val(search))
else:
    print("The phone number is not found")
