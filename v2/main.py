# Importing libs
from tkinter import *
from tkinter import messagebox
from tkinter import Toplevel
import secrets

# Initialize Definitions
def drawRandom():
    # Get Input
    names = NameArea.get("1.0", END).split("\n")
    reasons = ReasonArea.get("1.0", END).split("\n")
    nominators = NominatorArea.get("1.0", END).split("\n")
    if (not(len(names) == len(reasons))) or (not(len(reasons) == len(nominators))):
        messagebox.showerror("Dataset Error", "The amount of data in each column is not the same.")
    else:
        allPeople = []
        for i in range(len(names)):
            if i < len(names)-1: allPeople.append([names[i], reasons[i], nominators[i]])
        ##print(allPeople)
    # Get random choices
    try: numberOfPeople = int(PeopleNumArea.get("1.0", END))
    except: messagebox.showerror("Randomizer Error", "The amount of people to draw must be a number.")
    finalPeople = []
    for i in range(numberOfPeople):
        finalPeople.append(allPeople.pop(allPeople.index(secrets.choice(allPeople))))  ### Write custom function later to tidy up code
    # Result Window
    output = ""
    for person in finalPeople:
        output+=("{person}: {reason} - {who}\n".format(person=person[0], reason=person[1], who=person[2]))
    outFile = open("output.txt", "w")
    outFile.write(output)
    outFile.close()
    resultWindow = Toplevel()
    resultWindow.geometry("400x300")
    resultWindow.iconbitmap("superMario.ico")
    resultWindow.title("Results")
    resultText = Text(resultWindow)
    resultText.place(x=10, y=10, width=380, height=280)
    resultText.insert(END, output)
    
def saveFunc(): ############## WIP
    names = NameArea.get("1.0", END).split("\n")
    reasons = ReasonArea.get("1.0", END).split("\n")
    nominators = NominatorArea.get("1.0", END).split("\n")
    if (not(len(names) == len(reasons))) or (not(len(reasons) == len(nominators))):
        messagebox.showerror("Dataset Error", "The amount of data in each column is not the same. Try seeing if one or more of the columns has an extra empty line at the bottom.")
    else:
        outFile = open("dataset.csv", "w")
        for i in range(len(names)):
            outStr = "{0},{1},{2}".format(names[i], reasons[i], nominators[i])
            outFile.write("{0}\n".format(outStr))
        outFile.close()
def loadFunc():
    inFile = open("dataset.csv", "r")
    names = ""
    reasons = ""
    nominators = ""
    for line in inFile:
        names += "{0}\n".format(line.strip("\n").split(",")[0])
        reasons += "{0}\n".format(line.strip("\n").split(",")[1])
        nominators += "{0}\n".format(line.strip("\n").split(",")[2])
    NameArea.delete("1.0", END)
    NameArea.insert(END, names[:-1])
    ReasonArea.delete("1.0", END)
    ReasonArea.insert(END, reasons[:-1])
    NominatorArea.delete("1.0", END)
    NominatorArea.insert(END, nominators[:-1])
def clearFunc():
    NameArea.delete("1.0", END)
    ReasonArea.delete("1.0", END)
    NominatorArea.delete("1.0", END)
  
# Initialize Tkinter
window = Tk()
window.title("Nomination Randomizer")
window.iconbitmap("superMario.ico")
width=600
height=450
window.geometry("{0}x{1}".format(width, height+20))
sX=width/400
sY=height/300
window.resizable(False, False)

# Initialize Menu
menu = Menu(window)
dataset_menu = Menu(menu, tearoff=0)
dataset_menu.add_command(label="Save", command=saveFunc)
dataset_menu.add_command(label="Load", command=loadFunc)
dataset_menu.add_command(label="Clear", command=clearFunc)
menu.add_cascade(label="Dataset", menu=dataset_menu)
window.config(menu=menu)

##### Window Box #####
# Input Boxes & Labels
NameArea = Text(window)
NameArea.place(x=10*sX, y=25*sY, height=200*sY, width=120*sX)
NameArea.insert(END, "")
NameAreaLabel = Label(window, text="Student name:", font="Arial {0}".format(int(8*sY)))
NameAreaLabel.place(x=10*sX, y=2.5*sY)

ReasonArea = Text(window)
ReasonArea.place(x=140*sX, y=25*sY, height=200*sY, width=120*sX)
ReasonAreaLabel = Label(window, text="Reason for nomination:", font="Arial {0}".format(int(8*sY)))
ReasonAreaLabel.place(x=140*sX, y=2.5*sY)

NominatorArea = Text(window)
NominatorArea.place(x=270*sX, y=25*sY, height=200*sY, width=120*sX)
NominatorAreaLabel = Label(window, text="Name of the nominator:", font="Arial {0}".format(int(8*sY)))
NominatorAreaLabel.place(x=270*sX, y=2.5*sY)


PeopleNumArea = Text(window, font="Arial {0}".format(int(10*sY)))
PeopleNumArea.place(x=10*sX, y=245*sY, height=20*sY, width=380*sX)
PeopleNumAreaLabel = Label(window, text="Number of people to draw:", font="Arial {0}".format(int(8*sY)))
PeopleNumAreaLabel.place(x=10*sX, y=225*sY)

RandomizeButton = Button(window, text="Randomize", command=drawRandom)
RandomizeButton.place(x=165*sX, y=270*sY, height=25*sY, width=70*sX)#height 25 width 70
RandomizeButton['font'] = "Arial {0}".format(int(8*sY))

# Main loop to keep program running
window.mainloop()
