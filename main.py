from tkinter import *
import tkinter.font as tkFont

import random

import os 
from pathlib import Path, PurePath

global BASE_PATH
BASE_PATH = Path(__file__).parents[0]

#find icon path
iconPath = Path(PurePath(BASE_PATH, 'Icons'))
windowIconPath = Path(PurePath(iconPath, 'CCT.ico'))
aboutIconPath = Path(PurePath(iconPath, 'about.ico'))
gearsIconPath = Path(PurePath(iconPath, 'gears.ico'))

#initialise various variables used
lbValues = []
recordcolour = 0
showCoords = 0
colour = 1
time = 30.0
total = 0
score = 0
chosensquare = 0
begun = 0
k = 0
sessionbest10 = 0
sessionbest30 = 0
sessionbest60 = 0
newrecordtimer = 0
gameOver = 1
nextColour = ""
stopTimer = 0

#initialise a parent window called top
top = Tk()

screenWidth = top.winfo_screenwidth()
screenHeight = top.winfo_screenheight()

top.configure(bg = "gray80")
top.wm_title("Chess Coordinate Trainer")
top.resizable(width=FALSE, height=FALSE)
top.wm_iconbitmap(windowIconPath)

#centre top window
top.geometry("%dx%d+%d+%d" % ((755, 848) + ((screenWidth / 2.0) - 378, (screenHeight / 2.0) - 424)))

#define fonts
helv8 = tkFont.Font(family='Helvetica', size=8)
helv50 = tkFont.Font(family='Helvetica', size=50)
bottomLabelFont10 = tkFont.Font(family='Helvetica', size=10)

#create all the chessboard squares as Tkinter buttons

squares = ["A1","A2","A3","A4","A5","A6","A7","A8","B1","B2","B3","B4","B5","B6","B7","B8","C1","C2","C3","C4","C5","C6","C7","C8","D1","D2","D3","D4","D5","D6","D7","D8","E1","E2","E3","E4","E5","E6","E7","E8","F1","F2","F3","F4","F5","F6","F7","F8","G1","G2","G3","G4","G5","G6","G7","G8","H1","H2","H3","H4","H5","H6","H7","H8"]

A1 = Button(top, height = 5, width = 12, command = lambda: click("A1"), bg = "Olive Drab", anchor = "sw", text = "A1")
A2 = Button(top, height = 5, width = 12, command = lambda: click("A2"), bg = "Light Yellow", anchor = "sw", text = "2")
A3 = Button(top, height = 5, width = 12, command = lambda: click("A3"), bg = "Olive Drab", anchor = "sw", text = "3")
A4 = Button(top, height = 5, width = 12, command = lambda: click("A4"), bg = "Light Yellow", anchor = "sw", text = "4")
A5 = Button(top, height = 5, width = 12, command = lambda: click("A5"), bg = "Olive Drab", anchor = "sw", text = "5")
A6 = Button(top, height = 5, width = 12, command = lambda: click("A6"), bg = "Light Yellow", anchor = "sw", text = "6")
A7 = Button(top, height = 5, width = 12, command = lambda: click("A7"), bg = "Olive Drab", anchor = "sw", text = "7")
A8 = Button(top, height = 5, width = 12, command = lambda: click("A8"), bg = "Light Yellow", anchor = "sw", text = "8")
B1 = Button(top, height = 5, width = 12, command = lambda: click("B1"), bg = "Light Yellow", anchor = "sw", text = "B")
B2 = Button(top, height = 5, width = 12, command = lambda: click("B2"), bg = "Olive Drab", anchor = "sw")
B3 = Button(top, height = 5, width = 12, command = lambda: click("B3"), bg = "Light Yellow", anchor = "sw")
B4 = Button(top, height = 5, width = 12, command = lambda: click("B4"), bg = "Olive Drab", anchor = "sw")
B5 = Button(top, height = 5, width = 12, command = lambda: click("B5"), bg = "Light Yellow", anchor = "sw")
B6 = Button(top, height = 5, width = 12, command = lambda: click("B6"), bg = "Olive Drab", anchor = "sw")
B7 = Button(top, height = 5, width = 12, command = lambda: click("B7"), bg = "Light Yellow", anchor = "sw")
B8 = Button(top, height = 5, width = 12, command = lambda: click("B8"), bg = "Olive Drab", anchor = "sw")
C1 = Button(top, height = 5, width = 12, command = lambda: click("C1"), bg = "Olive Drab", anchor = "sw", text = "C")
C2 = Button(top, height = 5, width = 12, command = lambda: click("C2"), bg = "Light Yellow", anchor = "sw")
C3 = Button(top, height = 5, width = 12, command = lambda: click("C3"), bg = "Olive Drab", anchor = "sw")
C4 = Button(top, height = 5, width = 12, command = lambda: click("C4"), bg = "Light Yellow", anchor = "sw")
C5 = Button(top, height = 5, width = 12, command = lambda: click("C5"), bg = "Olive Drab", anchor = "sw")
C6 = Button(top, height = 5, width = 12, command = lambda: click("C6"), bg = "Light Yellow", anchor = "sw")
C7 = Button(top, height = 5, width = 12, command = lambda: click("C7"), bg = "Olive Drab", anchor = "sw")
C8 = Button(top, height = 5, width = 12, command = lambda: click("C8"), bg = "Light Yellow", anchor = "sw")
D1 = Button(top, height = 5, width = 12, command = lambda: click("D1"), bg = "Light Yellow", anchor = "sw", text = "D")
D2 = Button(top, height = 5, width = 12, command = lambda: click("D2"), bg = "Olive Drab", anchor = "sw")
D3 = Button(top, height = 5, width = 12, command = lambda: click("D3"), bg = "Light Yellow", anchor = "sw")
D4 = Button(top, height = 5, width = 12, command = lambda: click("D4"), bg = "Olive Drab", anchor = "sw")
D5 = Button(top, height = 5, width = 12, command = lambda: click("D5"), bg = "Light Yellow", anchor = "sw")
D6 = Button(top, height = 5, width = 12, command = lambda: click("D6"), bg = "Olive Drab", anchor = "sw")
D7 = Button(top, height = 5, width = 12, command = lambda: click("D7"), bg = "Light Yellow", anchor = "sw")
D8 = Button(top, height = 5, width = 12, command = lambda: click("D8"), bg = "Olive Drab", anchor = "sw")
E1 = Button(top, height = 5, width = 12, command = lambda: click("E1"), bg = "Olive Drab", anchor = "sw", text = "E")
E2 = Button(top, height = 5, width = 12, command = lambda: click("E2"), bg = "Light Yellow", anchor = "sw")
E3 = Button(top, height = 5, width = 12, command = lambda: click("E3"), bg = "Olive Drab", anchor = "sw")
E4 = Button(top, height = 5, width = 12, command = lambda: click("E4"), bg = "Light Yellow", anchor = "sw")
E5 = Button(top, height = 5, width = 12, command = lambda: click("E5"), bg = "Olive Drab", anchor = "sw")
E6 = Button(top, height = 5, width = 12, command = lambda: click("E6"), bg = "Light Yellow", anchor = "sw")
E7 = Button(top, height = 5, width = 12, command = lambda: click("E7"), bg = "Olive Drab", anchor = "sw")
E8 = Button(top, height = 5, width = 12, command = lambda: click("E8"), bg = "Light Yellow", anchor = "sw")
F1 = Button(top, height = 5, width = 12, command = lambda: click("F1"), bg = "Light Yellow", anchor = "sw", text = "F")
F2 = Button(top, height = 5, width = 12, command = lambda: click("F2"), bg = "Olive Drab", anchor = "sw")
F3 = Button(top, height = 5, width = 12, command = lambda: click("F3"), bg = "Light Yellow", anchor = "sw")
F4 = Button(top, height = 5, width = 12, command = lambda: click("F4"), bg = "Olive Drab", anchor = "sw")
F5 = Button(top, height = 5, width = 12, command = lambda: click("F5"), bg = "Light Yellow", anchor = "sw")
F6 = Button(top, height = 5, width = 12, command = lambda: click("F6"), bg = "Olive Drab", anchor = "sw")
F7 = Button(top, height = 5, width = 12, command = lambda: click("F7"), bg = "Light Yellow", anchor = "sw")
F8 = Button(top, height = 5, width = 12, command = lambda: click("F8"), bg = "Olive Drab", anchor = "sw")
G1 = Button(top, height = 5, width = 12, command = lambda: click("G1"), bg = "Olive Drab", anchor = "sw", text = "G")
G2 = Button(top, height = 5, width = 12, command = lambda: click("G2"), bg = "Light Yellow", anchor = "sw")
G3 = Button(top, height = 5, width = 12, command = lambda: click("G3"), bg = "Olive Drab", anchor = "sw")
G4 = Button(top, height = 5, width = 12, command = lambda: click("G4"), bg = "Light Yellow", anchor = "sw")
G5 = Button(top, height = 5, width = 12, command = lambda: click("G5"), bg = "Olive Drab", anchor = "sw")
G6 = Button(top, height = 5, width = 12, command = lambda: click("G6"), bg = "Light Yellow", anchor = "sw")
G7 = Button(top, height = 5, width = 12, command = lambda: click("G7"), bg = "Olive Drab", anchor = "sw")
G8 = Button(top, height = 5, width = 12, command = lambda: click("G8"), bg = "Light Yellow", anchor = "sw")
H1 = Button(top, height = 5, width = 12, command = lambda: click("H1"), bg = "Light Yellow", anchor = "sw", text = "H")
H2 = Button(top, height = 5, width = 12, command = lambda: click("H2"), bg = "Olive Drab", anchor = "sw")
H3 = Button(top, height = 5, width = 12, command = lambda: click("H3"), bg = "Light Yellow", anchor = "sw")
H4 = Button(top, height = 5, width = 12, command = lambda: click("H4"), bg = "Olive Drab", anchor = "sw")
H5 = Button(top, height = 5, width = 12, command = lambda: click("H5"), bg = "Light Yellow", anchor = "sw")
H6 = Button(top, height = 5, width = 12, command = lambda: click("H6"), bg = "Olive Drab", anchor = "sw")
H7 = Button(top, height = 5, width = 12, command = lambda: click("H7"), bg = "Light Yellow", anchor = "sw")
H8 = Button(top, height = 5, width = 12, command = lambda: click("H8"), bg = "Olive Drab", anchor = "sw")

Alist = [A1,A2,A3,A4,A5,A6,A7,A8]
Blist = [B1,B2,B3,B4,B5,B6,B7,B8]
Clist = [C1,C2,C3,C4,C5,C6,C7,C8]
Dlist = [D1,D2,D3,D4,D5,D6,D7,D8]
Elist = [E1,E2,E3,E4,E5,E6,E7,E8]
Flist = [F1,F2,F3,F4,F5,F6,F7,F8]
Glist = [G1,G2,G3,G4,G5,G6,G7,G8]
Hlist = [H1,H2,H3,H4,H5,H6,H7,H8]

columnlist = [Alist,Blist,Clist,Dlist,Elist,Flist,Glist,Hlist]
alpha = ["A","B","C","D","E","F","G","H"]

#place the buttons in a grid layout
for i in range(8):
	for j in range(8):
		columnlist[i][j].grid(row=8-j,column=i)

#configure the buttons for playing as white
def whiteButtons():
	global A1,A2,A3,A4,A5,A6,A7,A8,B1,B2,B3,B4,B5,B6,B7,B8,C1,C2,C3,C4,C5,C6,C7,C8,D1,D2,D3,D4,D5,D6,D7,D8,E1,E2,E3,E4,E5,E6,E7,E8,F1,F2,F3,F4,F5,F6,F7,F8,G1,G2,G3,G4,G5,G6,G7,G8,H1,H2,H3,H4,H5,H6,H7,H8
	
	for i in range(8):
		for j in range(8):
			columnlist[i][j].configure(text = "%s" %squares[8*(i) + j], command = lambda i=i, j=j: click("%s" %squares[8*(i) + j]), anchor = "sw")
	
	if showCoords == 0:
		for i in range(1, 8):
			for j in range(1, 8):
				columnlist[i][j].configure(text = "")
		A1.configure(text = "A1")
		for i in range(1, 8):
			Alist[i].configure(text = i+1)
		for i in range(1, 8):
			columnlist[i][0].configure(text = alpha[i])
	
	for i in range(8):
		for j in range(8):
			columnlist[i][j].grid(row=8-j,column=i)

#configure the buttons for playing as black
def blackButtons():
	global A1,A2,A3,A4,A5,A6,A7,A8,B1,B2,B3,B4,B5,B6,B7,B8,C1,C2,C3,C4,C5,C6,C7,C8,D1,D2,D3,D4,D5,D6,D7,D8,E1,E2,E3,E4,E5,E6,E7,E8,F1,F2,F3,F4,F5,F6,F7,F8,G1,G2,G3,G4,G5,G6,G7,G8,H1,H2,H3,H4,H5,H6,H7,H8
	
	for i in range(8):
		for j in range(8):
			columnlist[i][j].configure(text = "%s" %squares[8*(7-i) + 7-j], command = lambda i=i, j=j: click("%s" %squares[8*(7-i) + 7-j]), anchor = "ne")
	
	if showCoords == 0:
		for i in range(8):
			for j in range(8):
				columnlist[i][j].configure(text = "")
		H8.configure(text = "A1")
		for i in range(7):
			Hlist[i].configure(text = 8-i)
		for i in range(7):
			columnlist[i][7].configure(text = alpha[7-i])

#create a menu frame for the buttons along the top
menuframe = Frame(top, width = 200, height = 1, bg = "gray70")
menuframe.grid(row =0, column = 0, columnspan = 8, sticky = W)
menuFont = tkFont.Font(family='Helvetica', size=10, weight = 'bold')

startbutton = Button(menuframe, width = 33, height = 1, command = lambda: start(), text = "Start", font = 20, bg = "gray94")
aboutbutton = Button(menuframe, width = 33, height = 1, command = lambda: showAbout(), text = "About", bg = "gray94")
exitbutton = Button(menuframe, width = 33, height = 1, command = sys.exit, text = "Exit", bg = "gray94")

#place them in a grid layout
startbutton.grid(row=0, column=0)
aboutbutton.grid(row=0,column=4)
exitbutton.grid(row=0,column=6)

menuframe.grid_columnconfigure(7, minsize = 93)

#create labels for the elements under the board
aimbox = Label(top, width = 3, height = 1, bg = "White", text = "...")
scorebox = Label(top, width = 5, height = 1, text = "0/0", bg = "White", anchor = "w")
timebox = Label(top, width = 4, height = 1, text = "30.0", bg = "White", anchor = "w")
bestbox = Label(top, width = 3, height = 1, text = "0", bg = "White")

colourlabel = Label(top, width = 37, height = 1, fg = "Black", bg = "White", text = "White")
scorelabel  = Label(top, width = 12, height = 1, text = "Current Score:", anchor = "e", bg = "Orange")
bestlabel = Label(top, width = 12, height = 1, text = "Session Best:", anchor = "e", bg = "Orange")
timelabel = Label(top, width = 8, height = 1, text = "Time Left:", anchor = "e", bg = "Orange")
newRecordLabel = Label(top , width = 11, height = 1, bg = "gray80")

#when a new record is obtained, create a flashing "New Record!" label
def newRecordChanger():
	global recordcolour
	if recordcolour == 1:
		recordcolour = 2
		newRecordLabel.configure(text = "New Record!", bg = "Dodger Blue")
		top.after(600, newRecordChanger)
	elif recordcolour == 2:
		recordcolour = 1
		newRecordLabel.configure(bg = "White")
		top.after(600, newRecordChanger)
	elif recordcolour == 0:
		newRecordLabel.configure(bg = "gray80", text = "")

#place the elements under the board in a grid layout
aimbox.grid(row=11,column=3,rowspan=4,columnspan=2)
scorebox.grid(row=11,column=1, sticky = "e", padx = 10)
timebox.grid(row=11,column=7, sticky = "w")
bestbox.grid(row=12,column=1, sticky = "w", padx = 24)
colourlabel.grid(row=9,column=2,columnspan=4)
scorelabel.grid(row=11,column=0, sticky = "w", columnspan = 2)
bestlabel.grid(row=12,column=0, sticky = "w", columnspan = 2)
timelabel.grid(row=11,column=6, sticky = "e")
newRecordLabel.grid(row=12,column=1,columnspan=2, sticky = "e")

top.grid_rowconfigure(9, minsize = 43)
top.grid_rowconfigure(10, minsize = 1)
top.grid_rowconfigure(15, minsize = 9)

#set the fonts of the elements under the board
bottomBoxFont = tkFont.Font(family='Helvetica', size=13)
bottomLabelFont = tkFont.Font(family='Helvetica', size=13, weight = 'bold')

aimbox['font'] = helv50
startbutton['font'] = helv8
aboutbutton['font'] = helv8

colourlabel['font'] = bottomLabelFont
scorelabel['font'] = bottomLabelFont
bestlabel['font'] = bottomLabelFont
timelabel['font'] = bottomLabelFont
newRecordLabel['font'] = bottomLabelFont
scorebox['font'] = bottomBoxFont
timebox['font'] = bottomBoxFont
bestbox['font'] = bottomBoxFont

#creates a window that displays 'about' information
def showAbout():
	global aboutWindow
	try:
		aboutWindow.winfo_exists()
	except:
		aboutWindow = Tk()
		aboutWindow.geometry("%dx%d+%d+%d" % ((482, 270) + (top.winfo_x() + 378 - 241, top.winfo_y() + 65)))
		aboutWindow.resizable(width=FALSE, height=FALSE)
		aboutWindow.configure(bg = "gray96")
		aboutWindow.wm_title("About")
		aboutWindow.wm_iconbitmap(aboutIconPath)
		
		def close(): #using quit() would exit the entire program
			aboutWindow.destroy()
		
		closeButton = Button(aboutWindow, width = 10, height = 1, text = "Close", command = lambda: close(), bg = "Gray")
		
		aboutText = Label(aboutWindow, text = ' Created by ChessTeam during the winter of 2018.', width = 48, height = 12, bg = "White")
				
		aboutText.config(font=("Helvetica", 12))
		aboutText.grid(row=1,column=1, columnspan = 2)
		
		closeButton.grid(row=2,column=1, sticky = "e")
		aboutWindow.grid_columnconfigure(0, minsize = 22)
		aboutWindow.grid_columnconfigure(3, minsize = 22)
		aboutWindow.grid_rowconfigure(0, minsize = 22)
		aboutWindow.grid_rowconfigure(2, minsize = 22)

#check if the score is a session best or new record
def scorechecker(score):
	global sessionbest10, sessionbest30, sessionbest60, newrecordtimer
	global recordcolour
	if score > sessionbest10 and time == 10.0:
		newrecordtimer = 1
		sessionbest10 = score
		bestbox.configure(text = sessionbest10)
		if sessionbest10 > lbValues[0]:
			recordcolour = 1
			newRecordChanger()
			lbValues[0] = sessionbest10
	if score > sessionbest30 and time == 30.0:
		newrecordtimer = 1
		sessionbest30 = score
		bestbox.configure(text = sessionbest30)
		if sessionbest30 > lbValues[1]:
			recordcolour = 1
			newRecordChanger()
			lbValues[1] = sessionbest30
	if score > sessionbest60 and time == 60.0:
		newrecordtimer = 1
		sessionbest60 = score
		bestbox.configure(text = sessionbest60)
		if sessionbest60 > lbValues[2]:
			recordcolour = 1
			newRecordChanger()
			lbValues[2] = sessionbest60

#start the clock
def timeupdater():
	global k
	global gameOver
	global recordcolour
	if stopTimer == 0:
		if k < (time/0.1) - 1:
			timebox.configure(text = "%s" %(time - 0.1 -0.1*k))
			k += 1
			top.after(88, timeupdater)
		elif k == (time/0.1) - 1: #fixes weird timerbox bug
			timebox.configure(text = "0.0")
			recordcolour = 0
			newRecordLabel.configure(bg = "gray80", text = "")
			scorechecker(score)
			gameOver = 1
			aimbox.configure(text = "...")

#increment the score (called when correct square clicked)
def scoreupdater(score):
	global total
	total += 1
	scorebox.configure(text = "%d/%d" %(score, total))

def countdownTimer3():
	aimbox.configure(text = "3")
	top.after(500, countdownTimer2)

def countdownTimer2():
	aimbox.configure(text = "2")
	top.after(500, countdownTimer1)

def countdownTimer1():
	aimbox.configure(text = "1")
	top.after(500, countdownTimer0)

def countdownTimer0():
	global begun
	global stopTimer
	timebox.configure(text = time)
	begun = 1
	top.after(88, timeupdater)
	stopTimer = 0
	aimbox.configure(text = randomsquarereturner())

#start the game
def start():
    global stopTimer
    global k
    global begun
    global score
    global total
    global newrecordtimer
    global gameOver
    global recordcolour
    gameOver = 0
    begun = 0
    if newrecordtimer == 1:
        if time == 10.0:
            recordcolour = 0
            newRecordLabel.configure(bg = "gray80", text = "")
        if time == 30.0:
            recordcolour = 0
            newRecordLabel.configure(bg = "gray80", text = "")
        if time == 60.0:
            recordcolour = 0
            newRecordLabel.configure(bg = "gray80", text = "")
        newrecordtimer = 0
    scorechecker(score)
    score = 0
    total = 0
    stopTimer = 1
    scorebox.configure(text = "0/0")
    timebox.configure(text = time)
    k = 0
    countdownTimer3()

#return a random square
def randomsquarereturner():
    global chosensquare
    chosensquare = (random.choice(squares))
    return chosensquare

#called when a square is clicked
def click(square):
    global score
    global chosensquare
    global total
    if gameOver == 0:
        if square == chosensquare and begun == 1:
            score += 1
            randomsquarereturner()
            aimbox.configure(text = chosensquare)
        elif begun == 1:
            randomsquarereturner()
            aimbox.configure(text = chosensquare)
        if begun == 1:
            scoreupdater(score)
        if colour == 3:
            list = [1,2]
            if random.choice(list) == 1:
                whiteButtons()
                colourlabel.configure(fg = "Black", bg = "White", text = "White")
                aimbox.configure(fg = "Black", bg = "White")
            else:
                blackButtons()
                colourlabel.configure(fg = "White", bg = "Black", text = "Black")
                aimbox.configure(fg = "White", bg = "Black")

#loops the window so it doesn;t immediately disappear
top.mainloop()