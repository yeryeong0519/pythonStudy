from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

main = Tk()
main.title("test screen")
main.geometry("300x200")
main.resizable(False, False)

def test_click():  # Corrected function name
    name = tkinter.simpledialog.askstring("question", "enter your name")
    age = tkinter.simpledialog.askstring("question", "enter your age")
    if name and age:
        if int(age) > 19:  # Added a colon
            tkinter.messagebox.showwarning("warning", "go")
        else:
            tkinter.messagebox.showinfo("Welcome", name + ", welcome")  # Modified the message format
    else:
        tkinter.messagebox.showwarning("error", 'no input value')

btn = Button(main, text="입장여부", foreground="Blue", command=test_click)  # Corrected function name
btn.pack()

main.mainloop()
