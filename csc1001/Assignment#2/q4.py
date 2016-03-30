# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 15.10
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/3/30
#********************************************************
# The Question Four

def is_anagrams(string1, string2):
    if set(string1) == set(string2):
        return True
    return False


def get_a_string(input_display_string):
    string = input(input_display_string)
    if string.isalpha():
        return string
    else:
        return get_a_string(input_display_string)


if __name__ == '__main__':
    if is_anagrams(get_a_string('Please input the first string:'), get_a_string('Please input the second string:')):
        print('These two strings are anagrams!')
    else:
        print('These two strings are not anagrams!')