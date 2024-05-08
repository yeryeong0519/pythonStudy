from tkinter import *
import tkinter.messagebox
main = Tk()
main.title("test screen")
main.geometry("300x200")
main.resizable(False, False)
def testclick():
    if tkinter.messagebox.askyesno("question", "are you underage"):
        tkinter.messagebox.showwarning("warning", "get out")
    else:
        tkinter.messagebox.showinfo("환영", "어서오세요, 고객님")
btn = Button(main, text = "입장여부", foreground="Blue", command = testClick)
btn.pack()
main.mainloop