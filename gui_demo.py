# Tkinter GUI example
# Convert KM to Miles

from tkinter import *

window = Tk()  # create program window


def km_to_miles():
    txt1.delete(1.0, END)  # clear value first
    miles = float(entr1_value.get()) * 1.6
    txt1.insert(END, miles) # insert value at end


lbl1 = Label(window, text='Kilometers')
lbl1.grid(row=0, column=1)

lbl2 = Label(window, text='Miles')
lbl2.grid(row=0, column=2)

btn1 = Button(window, text='Convert', command=km_to_miles)  # command = function without brackets
btn1.grid(row=1, column=0)

entr1_value = StringVar()  # special string object with methods
entr1 = Entry(window, textvariable=entr1_value)
entr1.grid(row=1, column=1)

txt1 = Text(window, height=1, width=20)
txt1.grid(row=1, column=2)

# code must be between window = Tk() and mainloop
# or program will close down
window.mainloop()

