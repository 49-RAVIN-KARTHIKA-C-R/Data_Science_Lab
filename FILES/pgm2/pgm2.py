#2.	Write a program to append a file with the contents of another file

file1=input('Enter the name of first file:')
file2=input('Enter the name of second file:')
f1=open(file1,'r')
f2=open(file2,'r')
print('first file--before appending:',f1.read())
print('second file--before appending:',f2.read())
f1.close()
f2.close()

f1=open(file1,'a+')
f2=open(file2,'r')
f1.write(f2.read())

f1.seek(0)
f2.seek(0)
print('first file --- after apending:',f1.read())
print('second file --- after apending:',f2.read())
f1.close()
f2.close()

