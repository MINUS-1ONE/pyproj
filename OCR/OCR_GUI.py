# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:50:30 2019

@author: Administrator_MINUS

思路：设置一个list长度为40*40=1600 全初始化为0(a=[0]*1600) 因此矩阵一的列数也相应的变为1600 
"""

from ocr import OCRNeuralNetwork
import numpy as np
import copy
import tkinter as tki
import tkinter.messagebox as msgbox

class OCRGUI(tki.Frame):
    def __init__(self, master=None):
        tki.Frame.__init__(self, master)
        self.pack()
        self.master.title("WELCOME TO OCR GUI")
        self.master.geometry("350x300")
        self.createWeight()
        
        self._TRANSLATED_WIDTH = 40 
        self._PIXEL_WIDTH = 5 # TRANSLATED_WIDTH = Canvas.width / PIXEL_WIDTH 将200长度的画布分为40块 每块像素大小为5
        self.data = [0]*1600
        
    def createWeight(self):
        
        self.canvas = tki.Canvas(self, width=200, height=200, bg="blue")
        self.canvas.pack()
        self.canvas.bind("<B1-Motion>",self.paint)
        
        self.fm_digit = tki.Frame(self)
        self.digitLabel = tki.Label(self.fm_digit, text="digit:")
        self.digitLabel.pack(side="left")
        self.digitEntry = tki.Entry(self.fm_digit)
        self.digitEntry.pack(side="left")
        self.fm_digit.pack(side="bottom", pady=10)
        
    def paint(self, event):
        
        x1, y1 = (event.x - 1),(event.y - 1)
    
        x2, y2 = (event.x + 1),(event.y + 1)
        
        xPixel = event.x // self._PIXEL_WIDTH
        yPixel = event.y // self._PIXEL_WIDTH
        
        self.data[((xPixel - 1)  * self._TRANSLATED_WIDTH + yPixel) - 1] = 1
        
        self.canvas.create_oval(x1, y1, x2, y2, fill="white")
        
        
#if __name__ == '__main__':
orc_GUI = OCRGUI()
a = orc_GUI.data
orc_GUI.mainloop()
         



