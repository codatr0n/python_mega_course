# Tkinter GUI example
'''
Create a Python program that expects a kilogram input value and converts
that value to grams, pounds, and ounces when the user pushes the Convert button.
'''

from tkinter import *

window = Tk()  # create program window
window.title('Weight converter')

def kg_convert():
    txt1.delete(1.0, END)  # clear value first
    txt2.delete(1.0, END)
    txt3.delete(1.0, END)

    grams = float(entr1_value.get()) * 1000
    pounds = float(entr1_value.get()) * 2.20462
    ounces = float(entr1_value.get()) * 35.274

    txt1.insert(END, grams)  # insert value at end
    txt2.insert(END, pounds)
    txt3.insert(END, ounces)


lbl1 = Label(window, text='Kilogram')
lbl1.grid(row=0, column=0)
lbl2 = Label(window, text='Grams')
lbl2.grid(row=1, column=0)
lbl3 = Label(window, text='Pounds')
lbl3.grid(row=1, column=1)
lbl4 = Label(window, text='Ounces')
lbl4.grid(row=1, column=2)

btn1 = Button(window, text='Convert', command=kg_convert)  # command = function without brackets
btn1.grid(row=0, column=2)

entr1_value = StringVar()  # special string object with methods
entr1 = Entry(window, textvariable=entr1_value).grid(row=0, column=1)

txt1 = Text(window, height=1, width=20, borderwidth=1, relief='ridge')
txt1.grid(row=2, column=0)  # grams
txt2 = Text(window, height=1, width=20, borderwidth=1, relief='ridge')
txt2.grid(row=2, column=1)  # pounds
txt3 = Text(window, height=1, width=20, borderwidth=1, relief='ridge')
txt3.grid(row=2, column=2)  # ounces

# code must be between window = Tk() and mainloop
# or program will close down
window.mainloop()

