myfile = open('fruits.txt')
fruit_list = myfile.read().splitlines()
for f in fruit_list:
    print(len(f))

