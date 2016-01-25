# coding=utf-8
# ********************************************************
#	> OS     : Ubuntu 14.04
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/1/25
# ********************************************************
# Calculate PI approximately

# Method pi = 4 - 4/3 + 4/5 - 4/7 + ......

# Initialize pi/4 -> PI_4
PI_4 = 0
# PI_4 = 1 - 1/3 + 1/5 - 1/7 + ......
n = 2000  # Initialize the number n
i = 0
# i is the argument to count how many number we have added
while i < n:
    if (i % 2) == 0:  # You could try '%' in your terminal python
        PI_4 += (1 / (2 * i + 1))
    else:
        PI_4 -= (1 / (2 * i + 1))
    i += 1

print(PI_4 * 4)
