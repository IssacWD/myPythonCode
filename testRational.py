# coding=utf-8
#********************************************************
# > OS     : Windows / Cent OS
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/1/1 
#********************************************************
# A test for class Rational from Rational.py
import Rational

# Create and initialize two rational numbers r1 and r2
r1 = Rational.Rational(4,2)
r2 = Rational.Rational(2,3)

# Display results
print(r1,"+",r2,"=",r1 + r2)
print(r1,"+",r2,"=",r1.__add__(r2))
print(r1,"-",r2,"=",r1 - r2)
print(r1,"+",r2,"=",r1.__sub__(r2))
print(r1,"*",r2,"=",r1 * r2)
print(r1,"*",r2,"=",r1.__mul__(r2))
print(r1,"/",r2,"=",r1 / r2)
print(r1,"/",r2,"=",r1.__truediv__(r2))

print(r1,">",r2,"is",r1 > r2)
print(r1,">=",r2,"is",r1 >= r2)
print(r1,"<",r2,"is",r1 < r2)
print(r1,"<=",r2,"is",r1 <= r2)
print(r1,"==",r2,"is",r1 == r2)
print(r1,"!=",r2,"is",r1 != r2)

print("int(r2) is",int(r2))
print("float(r2) is",float(r2))

print("r2[0] is",r2[0])
print("r2[1] is",r2[1])