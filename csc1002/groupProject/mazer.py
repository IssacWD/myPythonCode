from tkinter import *
import pickle
import explorer  # Import explorer as a module and call its functions later.
import copy


# Use these global variables to enable the pre-provided functions.

'''Actually, you do not need to declare the global variables below here. You can either declare
them in the functions where it is assgined, or directly use these variables when assigning
them values in your main script.
The declaration is presented here only for better understanding of the coding.
'''
global currentPosition  # This is the current position
global root  # Define your Tk object as root
# maze contains the maze information loaded from your original secret maze
# file,
global maze
# identical to the maze information written to mazeFile.pkl, and changed when
# the additional brick is added. It contains values:
# 0: empty block which is not explored
# 1: brick
# 2: START or the current position
# 3: GOAL
# tempMaze contains the maze information with explored blocks. It will not be
global tempMaze
# written to mazeFile.pkl for read by explorer.py. Its difference with maze is
# only in the new value below:
# 4: the block is previously empty and has been explored.
# It is the Label object showing the current position in
global labelCurrentPositionExplorer
# explore.py. CommunicationMazerExplorer() will update it
# and thus we make it global variable
# The START and GOAL positions. They can be located in any two distinct
# positions
global START, GOAL
# of the maze, except for the positions


#(0) File read: only in initialization
# The function below read from the secret path .pkl file.
# START and GOAL can be located in any two distinct positions of the maze, except for the positions
# on boundary.
def LoadMazeFile():
    'Load from the initial secret maze file, and extract START and GOAL.'
    global maze, START, GOAL
    # For Host team: You can change to your .pkl file name.
    file = open('mazeFileForTest.pkl', 'rb')
    maze = pickle.load(file)
    file.close()
    for i in range(len(maze)):
        if 2 in maze[i]:
            START = (i, maze[i].index(2))
        if 3 in maze[i]:
            GOAL = (i, maze[i].index(3))


#(1) File write: only in initialization
# The functions below write the explorerPath.pkl for communication initialization with explorer.py.
# Just include it in the coding. You do not need to call it.

def InitializeExplorerPath():
    'Initialize explorerPath.pkl for explorer.py.   mazer.py write explorerPath.pkl only this time.'
    # Overwrite the previous path information.
    file = open('explorerPath.pkl', 'wb')
    pickle.dump([START], file)
    print('In Mazer: explorerPath.pkl initialized.')
    file.close()


# Initialize by calling LoadMazeFile() and InitializeExplorerPath()
def Initialization():
    # Call LoadMazeFile() to read from the original secret path file.
    LoadMazeFile()
    InitializeExplorerPath()  # Call InitializeExplorerPath()
    # to initialize explorerPath.pkl at the begining of your file.

Initialization()

# The function above read from the original secret path file, and the write to the explorerPath.pkl for
# communication initialization with explorer.py.
# Just include it in the coding. You do not need to call it again.


#(2) File write: in initialization
#(3) File write: when a new brick is added
# The function below is pre-provided for writing mazeFile.pkl.
# Call it at appropriate place to coordinate mazer.py to explorer.py
# communication.

def WriteMazeFile():
    'Write the global variable maze to mazeFile.pkl for explorer.py to read.'
    file = open('mazeFile.pkl', 'wb')
    pickle.dump(maze, file)
    file.close()

# The function above is pre-provided for writing mazeFile.pkl.
# Call it at appropriate place to coordinate mazer.py to explorer.py
# communication.


#(4) File read: every 0.1s approximately
# The functions below are pre-provided for read from explorerPath.pkl around every 0.1 second and update
# the global variable tempMaze and the GUI.
# -- ReadCurrentPosition(): read from explorerPath.pkl, and assign current position to the global variable
#    currentPosition. It is called in CommunicationMazerExplorer().
# -- CommunicationMazerExplorer(): read from explorerPath.pkl around every 0.1 second, and if there is move
#    to a new position, update the the global variable tempMaze and show it in the GUI.
# -- UpdateTempMaze(previousPosition, currentPosition): update the global variable tempMaze and show it in
# the GUI. !!! There is still need to write a function ReDraw to update
# the GUI.


# Use this function before the root.mainloop()
def CommunicationMazerExplorer():
    ''' This function checks the new current position from Explorer, updates the labelCurrentPositionExplorer in GUI,
stores the new current position in path, and updates the global variable tempMaze (ReDraw the GUI in function UpdateMaze()).
CommunicationMazerExplorer() will be called around every 100 mini seconds.
'''
    global currentPosition, path, InitialBricks, count
    if InitialBricks == CountBricks():
        Addclick()
    else:
        DeleteClick()
    previousPosition = currentPosition
    # The global currentPosition will be changed by the position information
    # in explorerPath.pkl
    ReadCurrentPosition()
    if previousPosition != currentPosition:
        count = count+1
    labelCurrentPositionExplorer.configure(text='In Explorer: \ncurrentPosition=(%s,%s)' % (currentPosition[0], currentPosition[1]),
                                           justify=CENTER)
    # labelCurrentPositionExplorer shows the current position feedback from
    # Explorer.

    if currentPosition != previousPosition:
        UpdateGUI(previousPosition, currentPosition)
        # This function only updates tempMaze, rather than maze, which is
        # changed only when you add a brick.

    # CommunicationMazerExplorer() will be called every 100 ms.
    root.after(100, CommunicationMazerExplorer)


def ReadCurrentPosition():
    '''Read the current position stored in currentPosition.pkl and assign to the global variable currentPosition.
After InitializeCommunicationFile(), only explorer.py can write currentPosition.pkl, and thus it is the latest current
position information after keyboard input. 
'''
    global currentPosition, path
    file = open('explorerPath.pkl', 'rb')
    path = pickle.load(file)
    currentPosition = path[len(path)-1]
    file.close()


def UpdateGUI(previousPosition, currentPosition):
    '''Update the global varialble tempMaze, and then update GUI by ReDraw().
This function is called in CommunicationMazerExplorer().
You may not need to call it in your coding.'''
    global tempMaze
    tempMaze[previousPosition[0]][previousPosition[1]] = 4
    tempMaze[currentPosition[0]][currentPosition[1]] = 2
    # For Host team: ReDraw will update the maze GUI. You need to write it. It
    # does not need to return anything.
    ReDraw()


# The function below counts the number of bricks in the maze. Call it when
# needed.

def CountBricks():
    'It counts the brick number in the global variable maze, and return it.'
    brickNumber = 0
    for mazeRow in maze:
        brickNumber += mazeRow.count(1)  # Add the number of 1s, i.e. bricks.
    return brickNumber

# The function above counts the number of bricks in the maze. Call it when
# needed.


#!!!Include the above code and use them in mazer.py. Do not modify it, unless instructed to do so.!!!


def ReDraw():
    global tempMaze, labelArray, colors, previousPosition, currentPosition
    tempMaze = copy.deepcopy(maze)
    for i in range(len(tempMaze)):
        for j in range(len(tempMaze[0])):
            labelArray[i][j].configure(bg=colors[tempMaze[i][j]])
    labelArray[previousPosition[0]][
        previousPosition[1]].configure(text=count, image='')
    labelArray[currentPosition[0]][
        currentPosition[1]].configure(image='myImage')
    labelArray[currentPosition[0]][currentPosition[1]].photo = myImage


def DrawAddedBlock():
    global tempMaze, labelArray, colors
    tempMaze = copy.deepcopy(maze)
    for i in range(len(tempMaze)):
        for j in range(len(tempMaze[0])):
            labelArray[i][j].configure(bg=colors[tempMaze[i][j]])


def Addclick():
    global tempMaze, maze, labelArray
    for i in range(len(tempMaze)):
        for j in range(len(tempMaze[0])):
            exec('def Click_%s_%s(event):\n\tmaze[%s][%s]=1\n\tDrawAddedBlock()\n\tprint(\
"In Mazer:New Mazer Block:",(%s,%s))\n\tprint("The New Block is Added")' % (i, j, i, j, i, j))
            exec(
                'labelArray[%s][%s].bind(\'<Button-1>\',Click_%s_%s)' % (i, j, i, j))


def DeleteClick():
    global tempMaze, maze, labelArray
    for i in range(len(tempMaze)):
        for j in range(len(tempMaze[0])):
            exec('def Click_%s_%s(event):\n\tNone' % (i, j))
            exec(
                'labelArray[%s][%s].bind(\'<Button-1>\',Click_%s_%s)' % (i, j, i, j))

InitialBricks = CountBricks()
WriteMazeFile()
ReadCurrentPosition()
count = 0
tempMaze = copy.deepcopy(maze)
labelArray = copy.deepcopy(tempMaze)
colors = ['white', 'black', 'yellow', 'blue', 'gray']
root = Tk()
h = len(tempMaze)
w = len(tempMaze[0])
root.geometry('%sx%s' % (w*40, (h+1)*40))
labelCurrentPositionExplorer = Label(
    root, text='In Explorer: \ncurrentPosition=(%s,%s)' % (currentPosition[0], currentPosition[1]))
labelCurrentPositionExplorer.place(x=320, y=0, width=160, height=40)
labelCurrentPositionMazer = Label(root, text='In Mazer: \ncurrentPosition=(%s,%s)' % (
    currentPosition[0], currentPosition[1]))
labelCurrentPositionMazer.place(x=0, y=0, width=160, height=40)
LabelBrick = Label(root, text='Brick#:\n%s' % CountBricks())
LabelBrick.place(x=160, y=0, width=160, height=40)
for i in range(h):
    for j in range(w):
        labelArray[i][j] = Label(root, bg=colors[tempMaze[i][j]])
        labelArray[i][j].place(x=40*j, y=40*(i+1), width=40, height=40)
myImage = PhotoImage(file='apple.gif')
labelArray[currentPosition[0]][currentPosition[1]].configure(image=myImage)
labelArray[currentPosition[0]][currentPosition[1]].photo = myImage
print('In Mazer:Start:', START)
print('In Mazer:End:', GOAL)


#!!!Include the code below and use it in mazer.py.

# To Host Team: We change the KeyPress event to KeyRelease event,
root.bind("<KeyRelease-Up>", explorer.KeyUp)
# to prevent from continuous KeyPress. When the key is released from
# the pressed state, the event will be activated.
root.bind("<KeyRelease-Down>", explorer.KeyDown)
root.bind("<KeyRelease-Left>", explorer.KeyLeft)
root.bind("<KeyRelease-Right>", explorer.KeyRight)
CommunicationMazerExplorer()

root.mainloop()
