# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:50:30 2019

@author: Administrator_MINUS

思路：设置一个list长度为40*40=1600 全初始化为0(a=[0]*1600) 因此矩阵一的列数也相应的变为1600 
"""

from ocr import OCRNeuralNetwork
import tkinter.messagebox as msgbox
from collections import namedtuple
import tkinter as tki
import numpy as np

HIDDEN_NODE_COUNT = 30

data_matrix = np.loadtxt(open('data.csv', 'rb'), delimiter = ',')
data_labels = np.loadtxt(open('dataLabels.csv', 'rb'))

data_matrix = data_matrix.tolist()
data_labels = data_labels.tolist()

nn = OCRNeuralNetwork(HIDDEN_NODE_COUNT, data_matrix, data_labels, training_indices = list(range(5000)))

class OCRGUI(tki.Frame):
    def __init__(self, master=None):
        tki.Frame.__init__(self, master)
        self.pack()
        self.master.title("WELCOME TO OCR GUI")
        self.master.geometry("350x300")
        self.createWeight()
        
        self._TRANSLATED_WIDTH = 20 #40 20
        self._PIXEL_WIDTH =  10 # 10 5 # TRANSLATED_WIDTH = Canvas.width / PIXEL_WIDTH, 将200长度的画布分为40块 每块像素大小为5
        
        self.data = [0]*400
            
        self.training_data_array = []
        
        
    def createWeight(self):
        
        self.canvas = tki.Canvas(self, width=200, height=200, bg="blue")
        self.canvas.pack()
        self.canvas.bind("<B1-Motion>",self.paint)
        
        self.fm_btn = tki.Frame(self)
        self.trainBtn = tki.Button(self.fm_btn, text="Train", command=self.train)
        self.testBtn = tki.Button(self.fm_btn, text="Test", command=self.test)
        self.resetBtn = tki.Button(self.fm_btn, text="Reset", command=self.reset)
        self.trainBtn.pack(side="left", ipady=1, padx=10, pady=2)
        self.testBtn.pack(side="left", ipady=1, padx=10, pady=2)
        self.resetBtn.pack(side="left", ipady=1, padx=10, pady=2)
        self.fm_btn.pack(side="bottom", pady=10)
        
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
        
        self.canvas.create_oval(x1, y1, x2, y2, fill="red")
        
    def train(self):
        
        if 1 not in self.data or self.digitEntry.get() is None:
            msgbox.showwarning(title="[WARNING]", message="Please type and draw a digit value in order to train the network")
        else:
            msgbox.showinfo(title="[INFO]", message="Sending training data to server...")
            self.training_data_array=[{"y0":self.data, "label":int(self.digitEntry.get())}]
            nn.train(self.training_data_array)
            nn.save()
    
    def test(self):
        if 1 not in self.data:
            msgbox.showwarning(title="[WARNING]",message="Please draw a digit in order to test the network")
        else:
            result = nn.predict(self.data)
            msgbox.showinfo(title="[PREDICT INFO]", message="The neural network predict you wrote a %d" % result)
    
    def reset(self):
        self.canvas.delete(tki.ALL)
        self.data = [0]*400
        
if __name__ == '__main__':
    ocr_GUI = OCRGUI()
    aa = ocr_GUI.data
    ocr_GUI.mainloop()
    
         



