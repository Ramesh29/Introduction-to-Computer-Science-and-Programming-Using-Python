

"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:


"""

s = "ramesh"
list = [ 'a', 'e', 'i', 'o', 'u']

count = 0
for c in s:
    if c in list:
        count = count + 1
        
print("Number of vowels:" , count)