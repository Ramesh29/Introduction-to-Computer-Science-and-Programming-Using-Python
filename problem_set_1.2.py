"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

"""

s = 'azcbobobegghaklbob'
w = 'bob'
count = 0
slen = len(s)
wlen = len(w)
for i in range(slen):
    if s[i] == 'b' and i + 2 < slen and s[i: i+wlen] == w:
        count = count + 1

print("Number of times bob occurs is: ", count)