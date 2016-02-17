# coding=utf-8
#********************************************************
# > OS     : Windows / Cent OS
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/1/13
#********************************************************

def get_a_str_of_number():
    str_of_number = input("Please input the string of number :")
    if judge_the_str(str_of_number):
        return str_of_number
    else:
        print("Please input the string of number again :", end = " ")
        return False

def judge_the_str(str_of_number):
    for x in str_of_number:
        if '0' <= x <= '9':
            continue
        else:
            return False
def get_list(str_of_number):
    list_of_number = []
    for x in str_of_number:
        list_of_number.append(x)
    return list_of_number

def transformation(list_of_number):
    transformed_list = []
    lenth_of_list_of_number = len(list_of_number)
    index_number = 0
    while len(transformed_list) < lenth_of_list_of_number:
        index_number += 1
        if index_number % 2 == 1:
            list_of_number.append(list_of_number[0])
            list_of_number.remove(list_of_number[0])
        else:
            transformed_list.append(list_of_number[0])
            list_of_number.remove(list_of_number[0])
    return transformed_list

def retransformation(list_of_number):
    # transformed_list = []
    pass

def main():
    module_of_transform = eval(input("Input 1 for key and 2 for diskey :"))
    str_number = get_a_str_of_number()
    while str_number == False or judge_the_str(str_number) == False:
        str_number = get_a_str_of_number()
    list_of_number = get_list(str_number)
    tansformed_list = transformation(list_of_number)
    print("The transformed string of number :", end = "")
    for x in tansformed_list:
        print(x, end = "")

main()