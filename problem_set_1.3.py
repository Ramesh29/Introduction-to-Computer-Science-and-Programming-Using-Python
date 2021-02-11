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