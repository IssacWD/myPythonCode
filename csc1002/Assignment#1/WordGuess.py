# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 14.04
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/2/4
#********************************************************
# Word Guess Game
import random


def get_input():
    char = input("Guess latter:")
    if len(char) > 1 or not char.isalpha():
        print('Wrong input, try again.')
        char = get_input()
    return char


def randomly_question():
    list_of_word = ['approve',
                    'alter',
                    'career',
                    'transform',
                    'exterior',
                    'petroleum',
                    'tendency',
                    'interfere',
                    'vacant',
                    'range',]
    return list([i, 0 ] for i in random.choice(list_of_word))


def display_word(list_of_word):
    for i in list_of_word:
        if i[1] == 0:
            print('_', end='')
        else:
            print(i[0], end='')
    print()


def change(char, word_list):
    for item in word_list:
        if item[0] == char and item[1] != 1:
            item[1] = 1
            break


def judge(word_list):
    for char_list in word_list:
        if char_list[1] == 0:
            return True
    return False


if __name__ == '__main__':
    word_list = randomly_question()
    display_word(word_list)
    index = 0
    while judge(word_list):
        change(get_input(), word_list)
        index += 1
        display_word(word_list)
    print("Congradulations!")
    print("You have made %s trials: %s correct; %s incorrect" % (index, len(word_list), index - len(word_list)))



