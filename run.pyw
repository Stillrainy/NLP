#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Author: Shuyuan Yang
# Filename: run.pyw

from tkinter import *
from match import section_similarity


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.text1 = Text(self, bd=3, width=80, height=8)
        self.text1.pack()
        self.text2 = Text(self, bd=3, width=80, height=8)
        self.text2.pack()
        self.button = Button(self, text="Match", command=self.upper)
        self.button.pack()
        self.result = Entry(self, width=20)
        self.result.pack()
        # 交互部分
        self.text1.insert(INSERT, "输入标准答案")
        self.text2.insert(INSERT, "输入学生答案")
        self.match = StringVar()
        self.match.set("相似度：")
        self.result.config(textvariable=self.match)

    def upper(self):
        str1 = self.text1.get("0.0", "end").strip('\n')
        str2 = self.text2.get("0.0", "end").strip('\n')
        self.match.set('相似度：{:.2%}'.format(section_similarity(str1, str2)))


if __name__ == '__main__':
    root = App()
    root.master.title("NLP Demo")
    root.master.geometry('600x300')
    root.master.resizable(width=False, height=False)
    root.mainloop()
