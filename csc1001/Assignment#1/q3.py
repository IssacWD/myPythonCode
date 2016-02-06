# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 14.04
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/2/5
#********************************************************
# The Question Three
m = eval(input("Enter an integer:"))
n = 1
if m <= 0:
    print("wrong input")
while n ** 2 < m:
    n += 1
print(n)
