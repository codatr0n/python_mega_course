# Merging Text Files (Practice)
# Section 3, Lecture 71
# Here is a tricky exercise.
#
# 1. Please download the three text files attached in this lecture and put them in a folder. The first text file contains the text Content1 . The second contains Content2 and the third Content3 .
#
# 2. You should create a Python script that generates a new text file which should contain the content of all three text files. So the generated file should have this content:
#
# Content1
# Content2
# Content3
#
# In other words, your Python script should merge the three text files.
#
# 3. Also, the name of the output file should be the current timestamp. Example:2017-11-01-13-57-39-170965.txt


from datetime import datetime

files = ['file1.txt', 'file2.txt', 'file3.txt']
content = []

content = ''

# open files and add text to content string
for file in files:
    content += open(file).read() + '\n'

# create filename from datetime.now()
now = datetime.now()
filename = now.strftime('%Y-%m-%d-%H-%M-%S-%f' + '.txt')

# save content to content.txt
with open('content.txt', 'w') as myfile:
    myfile.write(content)


