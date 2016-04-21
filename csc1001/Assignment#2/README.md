# CSC1001 Assignment #2 #
#####student ID:115010148
###1. Question 1###
The core code:
```python
#!q1.py
def get_next_guess(num, last_guess):
    next_guess = (last_guess + (num / last_guess)) / 2
    if abs(next_guess - last_guess) > accuracy_parameter:
        return get_next_guess(num, next_guess)
    else: return next_guess
```
It use recursion to find the next guess until it is closed to last guess enough.
###2. Question 2###
First of all, I defined a function to judge whether a number is prime number:
```python
#!q2.py
def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
```
And then, I def a function to judge whether a number is emirp number, it depends on `is_prime()`:
```python
#!q2.py
def is_emirp(number):
    if is_prime(number):
        reverse_number = int(str(number)[::-1])
        if is_prime(reverse_number):
            return True
    return False
```
At last, I set a deco function to print the n umber who is emirp, and print them ten numbers per line.:
```python
#!q2.py
def deco_display(func):
    count = [1]
    def print_number(number):
        if count[0] % 10 == 0:
            count[0] += 1
            print(format(number, '<8d'))
        else:
            count[0] += 1
            print(format(number, '<8d'), end='')
    return print_number

@deco_display
def print_ten_per_line(number):
    pass
```
###2. Question 3###
I set those function as demand:
```python
#!q3.py
def sum_of_double_even_place(list_even_place_number):
    sum = 0
    for number in list_even_place_number:
        sum += get_digit(number * 2)
    return sum

def get_digit(double_number):
    if double_number < 10: return double_number
    splited = list(str(double_number))
    return int(splited[0]) + int(splited[1])

def sum_of_odd_place(list_odd_place_number):
    return sum(list_odd_place_number)

def is_valid(number_str):
    odd_number_list = list()
    even_number_list = list()
    for index, value in enumerate(list(number_str[::-1])):
        if index % 2 == 0:
            odd_number_list.append(int(value))
        else:
            even_number_list.append(int(value))
    if (sum_of_double_even_place(even_number_list) + sum_of_odd_place(odd_number_list)) % 10 == 0:
        return True
    else:
        return False
```
###2. Question 4###
I use `set()`to find whether two strings are satisfied:
```python
#!q4.py
def is_anagrams(string1, string2):
    if set(string1) == set(string2):
        return True
    return False
```
If those two sets are equal, those are anagrams.
###2. Question 5###
First of all, I set a list to display the status of lockers. And I define a function to change it:
```python
#!q5.py
def change(n, locker_status):
    for i in range(n, len(locker_status), n + 1):
        locker_status[i] = not locker_status[i]
```
And change it from the second student(Iset init list is all `True`s):
```python
#！q5.py
for i in range(1, 100):
        change(i, locker_status)
```
And then print it.
###2. Question 6###
I give two solution of this question
(1) I calculate the permutations of 8 numbers(0 ~ 7), and judge whether it is the `Eight Queens`. If it is, append it into list. And choose one to print. The core code is:
```python
#!q6.py
def get_valid_solution():
    valid_solutions_list = list()
    queens_status_list = list(range(8))
    for vec in itertools.permutations(queens_status_list):
        if (len(set(vec[i] - i for i in range(8))) == 8) and (len(set(vec[i] + i for i in range(8))) == 8):
            valid_solutions_list.append(vec)
    return random.choice(valid_solutions_list)
```
(2) I def a conflict function to judge whether it is fine to set a Queen:
```python
#！q(2).py
def is_conflict(status_tuple, next_row_place):
    this_row_number = len(status_tuple)
    if next_row_place in status_tuple: return True
    for row_number, place in enumerate(status_tuple):
        left_right = place - row_number ; right_left = place + row_number
        if (next_row_place - this_row_number == left_right) or (next_row_place + this_row_number == right_left):
            return True
    return False
```
And then I use yeild to find a solution, the core code is:
```python
#!q(2).py
def generater(queen_number, status_tuple=()):
    for position in range(queen_number):
        if not is_conflict(status_tuple, position):
            if len(status_tuple) == queen_number - 1:
                yield (position,)
            else:
                for next_result in generater(queen_number, status_tuple + (position,)):
                    yield (position,) + next_result

```