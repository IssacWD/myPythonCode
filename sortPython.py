# coding=utf-8
#********************************************************
# > OS     : Linux CentOS 6.5 / Windows
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/1/3
#********************************************************
# A python file to practice sort
# Get a list of number
def get_list():
    number_for_numbers = eval(input("How many numbers do you have? :"))
    list_of_number = []
    get_how_input = eval(input("How do you want to input? 1 for a list and 2 for input them step by step"))
    if get_how_input == 2:
        for i in range(number_for_numbers):
            temp = eval(input("Please input ",i,"number"))
            list_of_number.append(temp)
    elif get_how_input == 1:
        string_of_numbers = input("Please input the numbers splited by space :")
        list_of_number = string_of_numbers.split()
        for i in range(list_of_number):
            list_of_number[i] = eval(list_of_number[i])
    return list_of_number

def sort_bucket(list_of_number):
    reversed_number = list_of_number.reverse()
    max_number = reversed_number[0]
    buckets = [0] * max_number
    for number in list_of_number:
        buckets[number] += 1
    sorted_list = []
    get_index = 0
    for i in buckets:
        get_index += 1
        if i != 0:
            for j in range(i):
            sorted_list.append(get_index)
    return sorted_list

def sort_bubble(list_of_number):
    number_of_numbers = len(list_of_number)
    for i in range(number_of_numbers):
        for j in range(i + 1, number_of_numbers):
            if list_of_number[j] < list_of_number[i]:
                list_of_number[i], list_of_number[j] = list_of_number[j], list_of_number[i]
    sorted_list = list_of_number
    return sorted_list

def sort_insertion(list_of_number):
    pass

def sort_quicksort(list_of_numbre):
    pass

def print_list(sorted_list):
    for i in range(len(sorted_list)):
        print(sorted_list[i])

def main():
    list_of_number = get_list()
    cmp_list = []
    sorted_bucket = sort_bucket(list_of_number)
    sorted_bubble = sort_bubble(list_of_number)
    sorted_insertion = sort_insertion(list_of_number)
    sorted_quicksort = sort_quicksort(list_of_number)
    cmp_list.append(sorted_bucket)
    cmp_list.append(sorted_bubble)
    cmp_list.append(sorted_insertion)
    cmp_list.append(sorted_quicksort)
    print_list(cmp_list)

main()


