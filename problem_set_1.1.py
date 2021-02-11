

s = "ramesh"
list = [ 'a', 'e', 'i', 'o', 'u']

count = 0
for c in s:
    if c in list:
        count = count + 1
        
print("Number of vowels:" , count)