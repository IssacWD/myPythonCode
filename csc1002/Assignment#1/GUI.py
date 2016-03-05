# coding=utf-8
# ********************************************************
#   > OS     : Ubuntu 14.04
# 	> Author : JasonGUTU
# 	> Mail   : intergujinjin@foxmail.com
# 	> Time   : 2016/2/26
# *******************************************************
from tkinter import *
import sys
from WordGuess import *


def _get_img(char):
    if char.isalpha():
        return 'alpha/%s.jpg' % char
    else:
        return 'alpha/what.jpg'

class GUI:
    def __init__(self):
        root = Tk()
        root.title('Word Guess!')

        self._input_list = list()
        self._word_list = randomly_question()

        def input_char(event):
            if len(event.char) > 1 or not event.char.isalpha():
                self._input_list.append('0')

        frame_left = Frame(root)
        word_img = PhotoImage(file=_get_img(self._input_list[-1] if len(self._input_list) >= 1 else '0'))
        entry = Entry(frame_left)








def end():

def change(char, word_list):
    for item in word_list:
        if item[0] == char and item[1] != 1:
            item[1] = 1
            break
def quit():
    print('About to quit :( \n   ByeBye!')
    sys.exit()
def return_word(list_of_word):
    word_str = ''
    for i in list_of_word:
        if i[1] == 0:
            word_str += '_'
        else:
            word_str += i[0]
    return word_str
def judge(word_list):
    for char_list in word_list:
        if char_list[1] == 0:
            return True
    return False


if __name__ == '__main__':
    root = GUI()
