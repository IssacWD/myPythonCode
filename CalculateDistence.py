# coding=utf-8
#********************************************************
# > OS     : Windows / Cent OS
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/1/2
#********************************************************
import turtle

# Calculate the distance


def distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[1]) ** 2) ** 0.5

# Find the max and min of distance


def findMaxAndMin(row, FindWhat):
    # Define temp var
    #  Value point1 point2 numberOfPonit1 numberOfPoint2
    maximum = [0, 0, 0, 0, 0]
    minimum = [0, 0, 0, 0, 0]
    # Start compare
    if FindWhat == 1:
        for i in range(len(row)):
            for j in range(i + 1, len(row)):
                if distance(row[i], row[j]) >= maximum[0]:
                    maximum[0] = distance(row[i], row[j])
                    maximum[1] = row[i]
                    maximum[2] = row[j]
                    maximum[3] = i
                    maximum[4] = j
        return maximum
    elif FindWhat == 2:
        for i in range(len(row)):
            for j in range(i + 1, len(row)):
                if i == 0 and j == 1:
                    minimum[0] = distance(row[i], row[j])
                if distance(row[i], row[j]) <= minimum[0]:
                    minimum[0] = distance(row[i], row[j])
                    minimum[1] = row[i]
                    minimum[2] = row[j]
                    minimum[3] = i
                    minimum[4] = j
        return minimum


def findWhat():
    FindWhat = input("Select the maximum(1) or the minimum(2)")
    return FindWhat


def getInputlist():
    # Get the number of points
    numberOfPoints = eval(input("How many points do you have?  :"))
    print()
    # Initialize a multidimensional list
    row = []
    for i in range(numberOfPoints):
        row.append([0, 0, 0])
    # Get the input for every point
    for i in range(numberOfPoints):
        print("Please input the ", i + 1,
              " point, splited by space :", end=" ")
        coordinateSTR = input()
        coordinate = coordinateSTR.split()
        for i in range(len(coordinate)):
            coordinate[i] = eval(coordinate[i])
        row.append(coordinate)
    return row

# Turtle the coordinate system


def turtleXYZ():
    turtle.goto(0, 0)
    turtle.pd()
    turtle.goto(0, 300)
    turtle.goto(6, 290)
    turtle.pu()
    turtle.goto(-6, 290)
    turtle.pd()
    turtle.goto(0, 300)
    turtle.goto(0, 0)
    turtle.goto(300, 0)
    turtle.goto(290, 6)
    turtle.pu()
    turtle.goto(290, -6)
    turtle.pd()
    turtle.goto(300, 0)
    turtle.goto(0, 0)
    turtle.rt(135)
    turtle.fd(212.1)
    turtle.lt(135)
    turtle.fd(5)
    turtle.bk(10)
    turtle.lt(90)
    turtle.fd(10)
    turtle.pu()
    turtle.goto(0, 0)

# Draw ponits


def drawPoints(row):
    turtle.seth(270)
    turtle.color("grey")
    for i in range(len(row)):
        tempX = row[i][0]
        temp = 1.414 * ((tempX * 212.1) / 300)
        turtlex = row[i][1] - temp
        turtley = row[i][2] - temp
        turtle.pu()
        turtle.goto(turtlex, turtley)
        turtle.pd()
        turtle.dot(4, "blue")
        turtle.write("p"+format(i, "2d"))
        turtle.fd(row[i][2])

# Display the result


def displayResult(Valuelist, FindWhat):
    if FindWhat == 1:
        print("In the points inputed by you, the maximum of distance is ",
              format(Valuelist[0], "10.2f"))
        print("These two points are :")
        print("Point", Valuelist[3 if Valuelist[3] < Valuelist[4] else 4], " ", Valuelist[
              1 if Valuelist[3] < Valuelist[4] else 2])
        print("Point", Valuelist[4 if Valuelist[3] < Valuelist[4] else 3], " ", Valuelist[
              2 if Valuelist[3] < Valuelist[4] else 1])
        # connectPoints()
    elif FindWhat == 2:
        print("In the points inputed by you, the minimum of distance is ",
              format(Valuelist[0], "10.2f"))
        print("These two points are :")
        print("Point", Valuelist[3 if Valuelist[3] < Valuelist[4] else 4], " ", Valuelist[
              1 if Valuelist[3] < Valuelist[4] else 2])
        print("Point", Valuelist[4 if Valuelist[3] < Valuelist[4] else 3], " ", Valuelist[
              2 if Valuelist[3] < Valuelist[4] else 1])
        # connectPoints()

# Connect two points
# def connectPoints(Valuelist):


def main():
    row = getInputlist()
    FindWhat = findWhat()
    Valuelist = findMaxAndMin(row, FindWhat)
    turtleXYZ()
    drawPoints(row)
    displayResult(Valuelist, FindWhat)
    get = input()

main()
