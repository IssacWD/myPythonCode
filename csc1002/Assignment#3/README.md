#CSC1002 Assignment #3#
##`Please read this before you run this program`##
#`I rewrite this program because it may not run well on Windows OS. So I cut down a lot of features. If you use Unix like OS, it will run very good! And this is write for Unix like OS. If you are TA or Windows user, 'How to run' will not fit you.`
###1. How to run###
#####Before running this program, please check whether your computer has DataBase `sqlite3`. This program depends on `sqlite3`.Defaultly, `sqlite3` will be installed when you install python, it is a buildin module in Python3.#####
1. This program need you to input arguments when you run it. **So please be sure that you run this program in CMD or Terminal.**
This program has such arguments:
```
-b [--both] :
The argument to output doc file. Program will not output doc file if this argument is not exist.
-db :
This argument is for setting the name of database file. The default name is 'word.db'. If you want database file name to be 'vocabulary.db', then input 'python vocabulary.py -dbvocabulary.db'.
-o :
This argument is for setting the name of doc file(need not to include '.doc'). The default name is 'Vocabulary.doc'. If you want doc file name to be 'Vocabulary.doc', then input 'python vocabulary.py -oVocabulary'. If you input this argument, it will output doc file.
-t :
This argument point out the name of the .txt file. The default name is 'TOEFL.txt' in this dir.
```
2. When you input the command in your CMD or Terminal, it will come out a web page of word list. And if your command has the argument '-b', '--both' or '-o', it will output a .doc file in the dir.

3. **To quick start, please input `python vocabulary.py -b`**

###2. About module`sqlite3`###
For practicing, I use sqlite3 to restore thw word data.
Before you use sqlite3, you shoud input it:
```python
#!vocabulary.py
import sqlite3
```
And then you need to connect the database:
```python
#!vocabulary.py
def init_DB():
	...
    db = sqlite3.connect(DB_file_name, check_same_thread=False)
    db.row_factory = sqlite3.Row
    curs = db.cursor()
    ...
```
Now you can execute SQL to database:
```python
#!vocabulary.py
curs.execute(SQL)
```
My words are all stored in the table 'word', it has six fields.
```
TABLE word
word    varchar		limit:255
rword	varchar		limit:255
mean    varchar		limit:255
eg		varchar		limit:255
synonym    varchar    limit:255
abtobym    varchar    limit:255
```
###3. About module`logging`###
For practicing, I use logging module to log the program.
The .log file will be 'Vocabulary.log'
You can check it to know if where has some exception.
###4. How it run###
Firstly, it will initialize a SQLite3 database. And then read the text file line by line. I use `re` module to compile word and the content. I set a buffer word and buffer content list. Once it read a new word then reset the buffer word and add the content list into database. The second field in list is `rword`. This is for reverse order. When we need to output a file, it will select from database order by word or rword. I set a html like style so that the ouput file has styles.