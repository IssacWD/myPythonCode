# coding=utf-8
#********************************************************
# > OS     : Windows
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2015/12/29 
#********************************************************

import turtle
import math
p1x = eval(input("Enter the x-coordinate of the point \" p1 \" :"))
p1y = eval(input("Enter the y-coordinate of the point \" p1 \" :"))
p2x = eval(input("Enter the x-coordinate of the point \" p2 \" :"))
p2y = eval(input("Enter the y-coordinate of the point \" p2 \" :"))
p3x = eval(input("Enter the x-coordinate of the point \" p3 \" :"))
p3y = eval(input("Enter the y-coordinate of the point \" p3 \" :"))
# Calculate the area
side1 = p1x * p2y - p2x * p1y
side2 = p2x * p3y - p3x * p2y
side3 = p3x * p1y - p1x * p3y
Area = 0.5 * (side1 + side2 + side3)
absArea = abs(Area)
# Draw the triangle
turtle.penup()
turtle.color("red")
turtle.goto(p1x,p1y)
turtle.pendown()
turtle.write("P1 ("+format(p1x,"4d")+","+format(p1y,"4d")+")")
turtle.goto(p2x,p2y)
turtle.write("P2 ("+format(p2x,"4d")+","+format(p2y,"4d")+")")
turtle.goto(p3x,p3y)
turtle.write("P3 ("+format(p3x,"4d")+","+format(p3y,"4d")+")")
turtle.goto(p1x,p1y)
turtle.penup()
turtle.goto(max(p1x,p2x,p3x),0)
turtle.pendown()
turtle.write("The area of this triangle is "+format(Area,"9.2f"))
