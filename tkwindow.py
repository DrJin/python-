#tkinter 실습
from tkinter import *
main = Tk()

main.title("Tk test") #title
main.geometry("300x200") #size

#위젯 종류는 15개
#위젯 생성 인수는 (부모 윈도우, 속성 키워드 인수s...) 순서
lbl = Label(main, text="label", font="Arial 20")
lbl.pack()

def makeClick(button): #button click function을 만드는 함
    def click():
        lbl["text"] = button["text"] #dictionary 방식으로 속성 변경 가능
    return click




apple = Button(main, text="Apple", foreground="Red")
appleClick = makeClick(apple)
apple.config(command=appleClick)
apple.pack()
orange =Button(main)
orange.pack()
orangeClick = makeClick(orange)
orange.config(text="Orange", foreground="Orange",command=orangeClick) #생성후의 속성 추가



main.mainloop()

#이후의 대화상자나 메뉴 그래픽은 필요하면 그때가서...
#tirtle 그래픽도 나중에 가서 Tirtle Demo 보면서...
#wxPython도 그때가서...
