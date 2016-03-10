#CSC1002 Assignment #2#
###1. Before Running Program###
When you run the program, you will see
```bash
============================
Please input function:
```
And you can input function string into it.
But it exist illegal input. When you try to input a equation string which has more than one '=' or dose not have '='. It will raise a exception:
```bash
==================================
Wrong Input! Please input an equation!
   AND THE PROGRAM WILL RESTART
==================================
```
Whne you try to input a function which variable are not 'x' and 'y', it will raise:
```bash
==================================
Wrong Input! The variable must be 'x' or 'y'
   AND THE PROGRAM WILL RESTART
==================================
```
If the linear equation your input has parallel lines, it will raise:
```bash
==================================
Wrong Input! Parallel lines exist!
   AND THE PROGRAM WILL RESTART
==================================
```
#####About the Exception#####
The Exception the program raised is all defined in the` InputError` which is inherited by `BaseException`:
```python
class InputError(BaseException):
    def __init__(self, value):
```
And the default selection is that the program will restart:
```python
pythonInterpreter = sys.executable
os.execl(pythonInterpreter, pythonInterpreter, * sys.argv)
```
If you want to exit, input 'terminate' after
```bash
If you want to exit, input 'terminate':
```
If the input is not 'terminate', the program will restart.
###2. Test Result###
Four groups of input in the lecture note, and the input as follow:
```bash
==================================
Please input function: x-y=-1
Please input function: y=2*x
Please input function: y=0
The area of the triangle is 1.0000
If you want to exit, input 'terminate':
==================================
Please input function: x-y=1
Please input function: 2x-2y=3
Please input function: y=2x+1
==================================
Wrong Input! Parallel lines exist!
   AND THE PROGRAM WILL RESTART
==================================
If you want to exit, input 'terminate':
==================================
Please input function: x-y=-1
Please input function: y=0
Please input function: x=1
The area of the triangle is 2.0000
If you want to exit, input 'terminate':
==================================
Please input function: y=-0.5x+1
Please input function: y=-2X
Please input function: x=y+1
The area of the triangle is 1.5000
If you want to exit, input 'terminate':terminate
===DONE===
```
###3. About The Code###
** The core method it calculate the point of two lines by using matrix**
**It will change every input function into this format**
$ax+by=c$
**And assume the lines**
$ax+by=e,cx+dy=f$
**And we could get the x, y of the point**
$x=\dfrac{\begin{vmatrix}e&b\\f&d\end{vmatrix}}{\begin{vmatrix}a&b\\c&d\end{vmatrix}},y=\dfrac{\begin{vmatrix}a&e\\c&f\end{vmatrix}}{\begin{vmatrix}a&b\\c&d\end{vmatrix}}$
**And if the two lines parallel**
$\begin{vmatrix}a&b\\c&d\end{vmatrix}=0$