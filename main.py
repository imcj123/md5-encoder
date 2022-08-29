from tkinter import *
import tkinter.filedialog
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, askopenfilenames, askdirectory
from tkinter.ttk import Treeview
import windnd
import md


def askfile():
    # 从本地选择一个文件，并返回文件的目录
    filename = tkinter.filedialog.askopenfilename()


width = 800
height = 600


class AboutMe(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.place(width=width, height=height)
        Label(self, text='Author: chenjie').grid()
        Label(self, text='Homepage: https://github.com/imcj123').grid()


# 文本转MD5的Frame页面
class Text2MD5(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.place(width=width, height=height)

        self.text = ScrolledText(self, undo=True)
        self.text.place(x=15, y=40, width=width - 15, height=300)

        self.md5text = Text(self)
        self.md5text.place(x=50, y=570, width=width - 100, height=30)

        self.ButtonGetText = Button(self, text='转化', command=self._get_text)
        self.ButtonGetText.place(x=240, y=530, width=40, height=40)

    def _get_text(self):
        text2transfer = self.text.get(1.0, 'end')
        md5string = md.get_str_md5(text2transfer)
        # 使其可编辑 再不可编辑 否则无法改变
        self.md5text.config(state=NORMAL)
        self.md5text.delete(1.0, 'end')
        self.md5text.insert(1.0, md5string)
        self.md5text.config(state=DISABLED)


def _dragged_file(files):
    msg = '\n'.join((item.decode('gbk') for item in files))
    showinfo('您拖放的文件', msg)


class Fill2MD5(Frame):
    def __init__(self, master):
        super().__init__()
        self.place(width=width, height=height)
        windnd.hook_dropfiles(self, func=_dragged_file)

        self.md5text = Text(self)
        self.md5text.place(x=50, y=550, width=width - 100, height=30)
        self.select_path = StringVar()
        Label(self, text='文件路径').grid()
        Entry(self, textvariable=self.select_path).grid()
        Button(self, text="选择多个文件", command=self.select_files).grid()
        # Entry(self,textvariable=)

        columns = ['No', 'File', 'md5']
        table = Treeview(
            master=self,
            height=10,
            columns=columns,
            show='headings'
        )
        table.heading('No', text='序号')
        table.heading('File', text='文件路径')
        table.heading('md5', text='md5值')

        table.column('No', width=50, anchor=S)
        table.column('No', width=200)
        table.column('No', width=200)

        table.grid()

    def select_files(self):
        # 多个文件选择
        selected_files_path = askopenfilenames()  # askopenfilenames函数选择多个文件
        print(selected_files_path)
        self.select_path.set('\n'.join(selected_files_path))  # 多个文件的路径用换行符隔开


if __name__ == '__main__':
    # 一些窗口的初始化
    tk = Tk()
    tk.title('编码器demo')
    tk.minsize(width, height)
    tk.state('normal')
    screenwidth = tk.winfo_screenwidth()
    screenheight = tk.winfo_screenheight()
    size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    tk.geometry(size_geo)
    tk.resizable(False, False)  # 禁止移动

    # 窗口居中，获取屏幕尺寸以计算布局参数，使窗口居屏幕中央

    # label = Label(tk, text="签名：", font=("等线", 25), fg="black")
    # label.grid()
    # entry = Entry(tk, font=("等线", 25), fg="black")
    # entry.grid(row=1, column=1)
    # 定位
    # label.grid()

    # text1 = Text2MD5(tk)
    text2 = Fill2MD5(tk)


    # canvas = Canvas(tk,
    #                 bg='#CDC9A5',
    #                 height=200,
    #                 width=300)
    # canvas.grid()
    # windnd.hook_dropfiles(canvas, func=dragged_file)

    # memu com
    def file2md5Click():
        text1 = Text2MD5(tk)
        text2.destroy()


    def aboutMeClict():
        text2.destroy()
        # text1.destory()
        AboutMe(tk)


    # text1.destroy()

    MainMenu = Menu(tk)
    MainMenu.add_command(label="关于", command=aboutMeClict)
    md5menu = Menu(MainMenu, tearoff=False)
    md5menu.add_command(label="文件转md5", command=file2md5Click)
    md5menu.add_command(label="文本转md5", command=file2md5Click)
    MainMenu.add_cascade(label="md5转码", menu=md5menu)
    # MainMenu.add_checkbutton(label="编辑")
    tk.config(menu=MainMenu)
    tk.mainloop()
