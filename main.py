from tkinter import *
import tkinter.filedialog 

from tkinter.messagebox import showinfo

import windnd


def dragged_file(files):
    msg = '\n'.join((item.decode('gbk') for item in files))
    showinfo('您拖放的文件', msg)

def askfile():
    # 从本地选择一个文件，并返回文件的目录
    filename = tkinter.filedialog.askopenfilename()
    if filename != '':
         lb.config(text= filename)
    else:
         lb.config(text='您没有选择任何文件')


# 一些窗口的初始化
tk = Tk()
tk.title('编码器demo')
width = 500
height = 400
tk.minsize(width, height)
tk.state('normal')
screenwidth = tk.winfo_screenwidth()
screenheight = tk.winfo_screenheight()
size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
tk.geometry(size_geo)
# 窗口居中，获取屏幕尺寸以计算布局参数，使窗口居屏幕中央

# memu com
MainMenu = Menu (tk)
MainMenu.add_command (label="关于")
MainMenu.add_command (label="编辑")
MainMenu.add_command (label="格式")
MainMenu.add_command (label="查看")
MainMenu.add_command (label="帮助")
tk.config(menu=MainMenu)


# label = Label(tk, text="签名：", font=("等线", 25), fg="black")
# label.grid()
# entry = Entry(tk, font=("等线", 25), fg="black")
# entry.grid(row=1, column=1)
# 定位
# label.grid()
tk.resizable(False, False)


canvas = Canvas(tk,
                bg='#CDC9A5',
                height=200,
                width=300)
canvas.grid()
canvas.pack()
windnd.hook_dropfiles(canvas, func=dragged_file)
tk.mainloop()