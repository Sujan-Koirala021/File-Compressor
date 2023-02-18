from tkinter import *
from tkinter import filedialog

win = Tk()
win.title("File Compressor")
win.iconbitmap("imgs/app_icon.ico")

#   Set window size
win.geometry("600x400")


win.filename = filedialog.askopenfilename(initialdir="C:/Users/user/Downloads", title = "Select A File", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
print(win.filename)

win.mainloop()