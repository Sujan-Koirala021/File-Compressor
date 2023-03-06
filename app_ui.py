import os
from tkinter import *
from tkinter import filedialog
import customtkinter
import tkinter.font as font

width = 600
height= 400
lightThemeBg = "#26242f"
darkThemeBg = "#dee4e7"

win = Tk()
win.title("File Compressor")
win.iconbitmap("imgs/app_icon.ico")

#   Set window size

win.geometry("{}x{}".format(width, height)) # same as win.geometry("600x400")
win.config(bg = darkThemeBg)

lightState = PhotoImage(file="imgs/light.png")
darkState = PhotoImage(file="imgs/dark.png")



lightMode = True
buttonFont = font.Font(family='Helvetica', size=18, weight='bold')


canvas = Canvas(win, width=300,bd=0, highlightthickness=0, relief='ridge', height=300, bg = darkThemeBg)
canvas.place(x = 50,y =  100)
homeImg = PhotoImage(file="imgs/home_img.png").subsample(2, 2)


# Create the image on the canvas without a box-like background
canvas.create_image(0, 0, anchor="nw", image=homeImg)




def switchMode():
    global lightMode
    if lightMode:
        button.config(image = darkState, bg = lightThemeBg, activebackground=lightThemeBg)
        canvas.config(bg = lightThemeBg)

        win.config(bg = lightThemeBg)
        lightMode = False
    else:
        button.config(image = lightState, bg = darkThemeBg, activebackground=darkThemeBg)
        canvas.config(bg = darkThemeBg)

        win.config(bg = darkThemeBg)
        lightMode = True
    







button = Button(win, image=lightState, bd = 0, bg = darkThemeBg, activebackground=darkThemeBg,font = buttonFont, command = switchMode)
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


# Use CTkButton instead of tkinter Button
compressButton = customtkinter.CTkButton(master=win, text_color=("black", "black"), text="Compress file",hover=True, hover_color="#0b6eca", width=170,height=50,border_width=0,corner_radius=0,text_font=("Courier", 12), command=openFileDialogForCompression)
compressButton.place(x = 3*width/4 , y =height/2 - 30, anchor=CENTER)

# extractButton = Button(win, text = "Extract File", command = openFileDialogForExtraction)
# extractButton.place(x = 3*width/4 , y =height/2 + 50)


# Use CTkButton instead of tkinter Button
extractButton = customtkinter.CTkButton(master=win, text="Extract file",text_color=("black", "black"),hover=True, hover_color="#0b6eca", width=170,height=50,border_width=0,corner_radius=0,text_font=("Courier", 12), command=openFileDialogForExtraction)
extractButton.place(x = 3*width/4 , y =height/2 + 50, anchor=CENTER)

win.mainloop()