from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

main = Tk()
main.title("test screen")
main.geometry("300x200")
main.resizable(False, False)

def test_click():
    name = tkinter.simpledialog.askstring("question", "enter your name")
    age = tkinter.simpledialog.askstring("question", "enter your age")
    if name and age:
        if int(age) > 19:
            tkinter.messagebox.showwarning("warning", "go")
        else:
            tkinter.messagebox.showinfo("Welcome", name + ", welcome")
    else:
        tkinter.messagebox.showwarning("error", 'no input value')

menubar = Menu(main)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Test", command=test_click)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=main.quit)
menubar.add_cascade(label="File", menu=filemenu)

main.config(menu=menubar)

main.mainloop()
