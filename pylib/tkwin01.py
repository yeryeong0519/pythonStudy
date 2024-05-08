from tkinter import *

main = Tk()   # 크로스 플랫폼을 지원하는 GUI 툴킷
main.title("파이썬 테스트")
main.geometry("300x200")
main.resizable(False, False)

lbl = Label(main, text="오후 수업중", font="Arial 20")  # 오타 수정 및 Label 생성 수정
lbl.pack()

def hello_click():  # 함수명 수정
    lbl["text"] = "안녕하세요"  

hello = Button(main, text="인사하기", foreground="Red", command=hello_click)  # 오타 수정
hello.pack()

def bye_click():  # 함수명 수정
    lbl["text"] = "잘가세요"  

bye = Button(main, text="보내기", foreground="Red", command=bye_click)  # 변수명 수정
bye.pack()

main.mainloop()
