"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

"""



s = 'azcbobobegghakl'


curfrom  = 0
curlen = 0
slen = len(s)

for i in range(slen):
    j = i
    while j+1 < slen and ord(s[j]) <= ord(s[j+1]):
        print(s[j])
        j = j + 1
    
    print(" ")
    wlen = j - i + 1 # missed the last char in the while loop
    if ( wlen > curlen):
        curlen = wlen
        curfrom = i
    
lword = s[curfrom: curfrom+curlen]
print( curfrom , curlen )
print("Longest substring in alphabetical order is: ", lword )