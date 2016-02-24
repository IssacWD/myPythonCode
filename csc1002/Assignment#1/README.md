#Assignment #1 CSC1002
###1. The test result
```bash
_____
Guess latter:a
_a___
Guess latter:e
_a__e
Guess latter:g
_a_ge
Guess latter:r
ra_ge
Guess latter:n
range
Congradulations!
You have made 5 trials: 5 correct; 0 incorrect
```
Program provide illegal input check. If you input more than one letter or the charactor you input is not a letter, it will raise:
```bash
Wrong input, try again.
```
And let you input again. Like this:
```bash
_____
Guess latter:sh
Wrong input, try again.
Guess latter:2
Wrong input, try again.
Guess latter:
```
###2. Explain for code
1. In the entrance of the code, program randomly choose a word from the word list which is given.
```python
#!WordGuess.py
word_list = randomly_question()
```
The function `randomly_question()` return a two-dimentional list. For example, if the question word is 'example', it will return:
```python
[['e', 0],
	['x', 0],
    ['a', 0],
    ['m', 0],
    ['p', 0],
    ['l', 0],
    ['e', 0]]
```
The number '0' distributed to every letter is for indicating letters' status. This disign aim to display word more conveniently.
2. Then we use `display_word()` function to display the word once.
```python
#!WordGuess.py
def display_word(list_of_word):
       for i in list_of_word:
           if i[1] == 0:
               print('_', end = '')
           else:
               print(i[0], end = '')
    print()
```
This function will check the number. If the number is 0, it indicates that this letter haven't be guessed acurrectly and it will print '_'. If the number is '1', it will print the letter.
3. Define an index value to count huw many times we have tried. Every time we input a letter successfully, it will plus one:
```python
#!WordGuess.py
index = 0
loop:
       index += 1
```
4. And then is the while loop.
```python
#!WordGuess.py
while judge(word_list):
       change(get_input(), word_list)
       index += 1
       display_word(word_list)
```
It referred twom function `judge()` and `change()`.
The function `judge()` will get the two-dimentional list of word and judge whether every letter in the word has been guessed successfully.
The function `change()` will get two arguments, the two-dimention list of word and the letter you input. It will check whether the letter is in the word, if so, it will change the number of that letter to 1.
```python
#!WordGuess.py
def change(char, word_list):
       for item in word_list:
           if item[0] == char and item[1] != 1:
               item[1] = 1
               break
```
5. When `judge()` function return `False`, which means every letter in the word has been guessed successfully, it will end the loop.
And the game is over, programe print your score.

