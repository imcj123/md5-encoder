from tkinter import *

class ChangePage:
    def __init__(self,root):
        self.root = root
        self.root.title('主页面')
        self.root.geometry('800x800')
        PageA(self.root)

class PageA:
    def __init__(self,root):
        self.root = root
        self.initPageA()

    def initPageA(self):
        # Frame 控件在屏幕上显示一个矩形区域，多用来作为容器。
        # 语法格式 Frame ( master, option, ... )
        # master: 框架的父容器。
        # options: 可选项，即该框架的可设置的属性。这些选项可以用键-值的形式设置，并以逗号分隔。
        self.initPageA = Frame(self.root,width=600,height=600,bg="pink")
        self.initPageA.pack()

        btn = Button(self.initPageA,text="切换到B页面",command=self.changePageB)
        btn.place(x=100,y=100)


    def changePageB(self):
        self.initPageA.destroy()
        PageB(self.root)

class PageB:
    def __init__(self,root):
        self.root = root
        self.initPageB()

    def initPageB(self):
        self.initPageB = Frame(self.root,width=300,height=600,bg="skyblue")
        self.initPageB.pack()

        btn = Button(self.initPageB,text="切换到A页面",command=self.changePageA)
        btn.place(x=100,y=100)

    def changePageA(self):
        self.initPageB.destroy()
        PageA(self.root)

if __name__ == "__main__":
    root = Tk()
    ChangePage(root)
    root.mainloop()