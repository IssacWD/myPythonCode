#Assignment CSC1001 #1
###1. About package AssTools
This package is wrote for **code reuse**. Because nearly every question need to judge whether the input is illegal. For higher accuracy, I use regular expression to match the input
```Python
#!AssTools/getInput.py
import re
```
The **getInput** class has the method which can help us to get currect input.
To use those methods, you need to **import** this in front of your code.
```Python
from AssTools.getInput import *method
```
**It provide illegal input check.**
If the input is illegal, it will print:
```bash
Unvalidated Input! Please input again!
```
And let you input again

Otherwise, function provides a argument 'length'. It acquiescently equal to 0 (no limit on number's length). If the number is out of range, it will raise:
```bash
Unvalidated Input! Please check the length of your input!
```

###2. Question 1

The **test result**:
```bash
[In]:
Enter the final account value:1000
Enter the annual interest rate:4.25
Enter the number of years:5
```
For some practical reasons, I used format() function to output formatted printing. The result is correct to two decimal places.
```bash
[Out]:
The initial value is 812.12 yuan
```

###3. Question 2
The **test result**:
```bash
[In]:
Enter an integer:3125
[Out]:
3
1
2
5
```
The core code:
```Python
#!q2.py
digits = ceil(log10(number))
output_list = list()
rest = number
for i in range(digits - 1, -1, -1):
    output_list.append(rest // (10 ** i))
    rest = rest % (10 ** i)
```
For using method ceil() and log10(), you need to import them before use them:
```Python
#!q2.py
from math import ceil, log10
```
###4. Question 3
The **test result:**
```bash
[In]:
Enter an integer:10
[Out]:
4
```

###5. Question 4
The **test result:**
```bash
[In]:
Please input a integer:5
[Out]:
m      m+1    m**(m+1)
1      2      1
2      3      8
3      4      81
4      5      1024
5      6      15625
```
I formated the output for look good.
###6. Question 5
```bash
[In]:
Enter an integer:100
[Out]:
The prime numbers smaller than 100 include:
2       3       5       7       11      13      17      19
23      29      31      37      41      43      47      53
59      61      67      71      73      79      83      89
97
```
The core code to judge whether a number is prime:
```python
def Judge(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
```
It is a simple algorithm for prime number judging. There many ways to optimize it's performance. But if the input number is not too big, the different will be small.
**Some illegal input error**
For example, if the number is smaller than 3, it will raise:
```bash
Do not have any number that meet the requirements!
```
###7. Question 6
The **test result:**
```bash
[In]:
Input the function:sin
Input a:1
Input b:10
Input the number of sub-intervals:10000
[Out]:
The result is 1.3793738814984595
```
**Some illegal input error**
If the function is not one of 'sin', 'cos' and 'tan', it will raise:
```bash
Does not support this function!
Please input one of 'sin' 'cos' 'tan'
```
And let you input again.

If you input a b which is smaller than a, it will raise:
```bash
a should be smaller than b
Please input a again:
```
And let you input again.