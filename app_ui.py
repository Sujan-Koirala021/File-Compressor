import os
from tkinter import *
from tkinter import filedialog

width = 600
height= 400

win = Tk()
win.title("File Compressor")
win.iconbitmap("imgs/app_icon.ico")

#   Set window size

win.geometry("{}x{}".format(width, height)) # same as win.geometry("600x400")
win.config(bg = "white")

lightState = PhotoImage(file="imgs/light.png")
darkState = PhotoImage(file="imgs/dark.png")

lightMode = True

def switchMode():
    global lightMode
    if lightMode:
        button.config(image = darkState, bg = "#26242f", activebackground="#26242f")
        win.config(bg = "#26242f")
        lightMode = False
    else:
        button.config(image = lightState, bg = "white", activebackground="white")
        win.config(bg = "white")
        lightMode = True
    

button = Button(win, image=lightState, bd = 0, bg = "white", activebackground="white", command = switchMode)
button.pack(padx=50, pady = 50)
button.place(x = width - 150, y = 10)


#   Make shorten button
# shortenButton['font'] = getFont("Helvetica", 12, "normal")



def openFileDialogForCompression():
    win.filename = filedialog.askopenfilename(initialdir=os.path.normpath("C://"), title = "Select A Text File", filetypes=(("text files", "*.txt"),)) # may use this for all files, ("all files", "*.*")
    pass

def openFileDialogForExtraction():
    win.filename = filedialog.askopenfilename(initialdir=os.path.normpath("C://"), title = "Select A Binary File", filetypes=(("binary files", "*.bin"),))
    pass

compressButton = Button(win, text = "Compress File", command = openFileDialogForCompression)
compressButton.place(x = 3*width/4 , y =height/2 - 30)

extractButton = Button(win, text = "Extract File", command = openFileDialogForExtraction)
extractButton.place(x = 3*width/4 , y =height/2 + 50)


win.mainloop()