text='Welcome to my Home'
print(text)

#indexing

print(text[0])
print(text[3])
print(text[0:7])
print(text[3:])
print(text[:])
print(text[-2])
print(text[-9])

# to count the number of characters in a string use len()

print(len(text))

# built in string methods
# .upper()->uppercase
# .lower()->lowercase
# .split()-> returns the list of words separated from the whitespace

print(text.upper())
print(text.lower())
print(text.split())

#string formatting with placeholder
lang='python'
print('we are learning %s.'%lang)
print('we are here to learn %s at %s'%(lang,'college'))

print('we are here to study',lang)