#CSC1001 Assignment #3
###### JasonGUTU
######ID: 115010148
---
###1. Question one
This is a class for flowers. It has some attributions, its name (type string), the number of petals(type integer), its price(type float). You can not run this python file directly. You can import this class if you want. You can initial this class with an argument 'name', if you have not indicate the name when you initial it , the defualt name will be `'init name'`. You can set the name with the method `setName()`. Other attributions all need to set with `set*` method.
```python
#!q1.py
class Flower:
    def __init__(self, name=None):

    def getName(self):

    def getPrice(self):

    def getNumberOfPetals(self):

    def setName(self, name):

    def setPrice(self, price):

    def setNumberOfPetals(self, number_of_petals):
```

###2. Question two
We have a polynomial class `Polynomial` to handle this question.

First of all, the `Polynomial` will get the polynomial string as arguments. and we can use the `get_derivative()` to get the derivative of this polynomial.
```python
# init the class
polynomial = Polynomial(polynomial_string)
# get derivative
polynomial.get_derivative()
```

###3. Question three
We have a class `River` to handle this question. when we init this river, we need three arguments: the length of river, the number of bears and the number of fishes. It will generate a river randomly.

And we have the `move()` method to do an iter. `move()` also can get an argument to indicate how many times you want to move at one time.

Class `River` has method `print_lines(times)`to display the movement at one time.
```python
#!q3.py
river = River(length_of_river, number_of_bear, number_of_fishes)
river.print_lines(times_you_want_see)
```
