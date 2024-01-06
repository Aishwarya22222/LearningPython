myfile=open('test.txt')
print(myfile)

print(myfile.read())

# seek()-> to print from the specific position
myfile.seek(6)
print(myfile.read())

# readlines()-> returns the list of the line of the file
myfile.seek(0)
print(myfile.readlines())

# \n -> new line

# writing to a file
#open('filename.ext','w+')
# w+ will truncate the original content of the file

myfile=open('test.txt','w+')
print(myfile)
myfile.write('this is the first line added from the write method')
myfile.seek(0)
print(myfile.read())

myfile.write('\nthis is the second line')
myfile.seek(0)
print(myfile.read())

myfile.close()

#appending to a file
newfile=open('hello.txt','a+')
print(newfile)
newfile.write('This is created using apend method')
newfile.seek(0)
print(newfile.read())

# remove the file
import os
#os.remove('abc.txt')
