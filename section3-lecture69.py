# TODO: The code prints out the output of the c_to_f  function multiple times in the terminal.
# For this exercise, please write the output in a text file instead of printing it out in the terminal.
# The text file content will look like this:
# 50.0
# -4.0
# 212.0
# Please don't write any message in the text file when input is lower than -273.15.

temperatures = [10, -20, -289, 100]


def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c* 9/5 + 32
        return f


with open('temperatures.txt', 'w') as myfile:
    for t in temperatures:
        temp = c_to_f(t)
        print(temp)
        if t > -273.15:
            myfile.write(str(temp) + '\n')


