#CSC1002 Assignment #4#
###How it run###
Firstly, in `__main__`, I defined two `StringVar()` objects to set the output in two labels.
```python
#!CalculatorGUI.py
if __name__ == '__main__':
     display_input = StringVar() ; display_output = StringVar()
```
And the `Label()` object:
```python
#!CalculatorGUI.py
label_input = Label(root,
                    bg='green',
                    borderwidth=3,
                    width=44,
                    height=4,
                    textvariable=display_input)
label_output = Label(root,
					 bg='yellow',
                     borderwidth=3,
                     width=44,
                     height=4,
                     textvariable=display_output)
```
And the buttons, I use `ttk()` and `for` to set buttons iterably.
We have the function to set the input string:
```python
#!CalculatorGUI.py
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
```
I use `eval()`method to calculate the input, if there is any expression, It will return 'Expression Error!'.
```python
#!CalculatorGUI.py
def calculate():
    """ use eval to get the calculation """
    try:
        form = display_input.get()
        res = eval(form)
        display_output.set(str(res))
    except:
        display_output.set("Expression Error!")
```


