from tkinter import *



def main():
	root = Tk()
	img = PhotoImage(file='alpha/wel.gif')
	imgLabel = Label(root, bg=img).grid()

	root.mainloop()

main()