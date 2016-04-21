# coding=utf-8
# ********************************************************
#   > OS     : Ubuntu 15.10
#   > Author : JasonGUTU
#   > Mail   : intergujinjin@foxmail.com
#   > Time   : 2016/4/6
# ********************************************************
from math import tan, cos, sin, sqrt  # import the math method
from tkinter import *  # import tkinter
from tkinter import ttk  # import ttk


def callback(num):
    """ function for change the display and judge the input """
    if num in ['7', '8', '9', '+', '4', '5', '6', '-', '(', '1', '2', '3', '*', ')', '0', '.', '/']:
        form = display_input.get() + num
        display_input.set(form)
    elif num == '<=':
        form = display_input.get()[:-1]
        display_input.set(form)
    elif num in ['tan', 'sin', 'cos', 'sqrt']:
        midware = '(%s)' % display_output.get()
        form = num + midware
        display_input.set(form)
        calculate()
    elif num == '1/x':
        form = '1/' + display_output.get()
        display_input.set(form)
        calculate()


def calculate():
    """ use eval to get the calculation """
    try:
        form = display_input.get()
        res = eval(form)
        display_output.set(str(res))
    except:
        display_output.set("Expression Error!")


def clear():
    """ clear all things """
    display_output.set("")
    display_input.set("")


if __name__ == '__main__':
    root = Tk()  # initial a root Tk()
    frame = Frame(root)  # build a frame
    root.title("Calculator GUI")
    display_input = StringVar()
    display_output = StringVar()  # set two display textvariables
    # two labels to display things
    label_input = Label(
        root, bg='green', borderwidth=3, width=44, height=4, textvariable=display_input)
    label_output = Label(root, bg='yellow', borderwidth=3,
                         width=44, height=4, textvariable=display_output)
    label_input.grid(row=0, column=0, columnspan=5)
    label_output.grid(row=1, column=0, columnspan=5)
    # set the buttons
    grid = ['7', '8', '9', '+', 'Clear', '4', '5', '6', '-',
            '(', '1', '2', '3', '*', ')', '0', '.', '<=', '/', '=', 'tan', 'cos', 'sin', 'sqrt', '1/x']
    for index, textChar in enumerate(grid):
        # local function for commend
        def cb(char=textChar):
            callback(char)
        # set buttons
        if textChar == 'Clear':
            ttk, Button(root, text=textChar, width=5, command=lambda: clear()).grid(
                row=3+index//5, column=index % 5)
        elif textChar == '=':
            ttk.Button(root, text=textChar, width=7, command=lambda: calculate()).grid(
                row=3+index//5, column=index % 5)
        else:
            ttk.Button(root, text=textChar, width=7, command=cb).grid(
                row=3+index//5, column=index % 5)
    root.mainloop()  # start mainloop
