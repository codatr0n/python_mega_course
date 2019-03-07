numbers = [1, 2, 3]

myfile = open('numbers.txt', 'a+')
for n in numbers:
    myfile.write(str(n) + '\n')

myfile.seek(0)
print(myfile.read())
myfile.close()
