from glob import glob
import argparse
from PIL import Image, ImageTk
import tkinter as tki
import scipy.misc as sm
import imutils
import cv2
import numpy as np

class PhotoBooth(tki.Frame):
	def __init__(self, master=None):
		tki.Frame.__init__(self, master)
		self.grid()
		self.master.title("Simplify PhotoBooth")
		self.master.geometry("760x420")
		self.createWeight()
		
		self.sample = []
		
	def createWeight(self):
		# 打开图片：直接打开图片和打开文件夹目录
		self.openBtn = tki.Button(self, text="Open", command=self.openimg).grid(row=0, pady=10)
		self.openDirBtn = tki.Button(self, text="Open Dir", command=self.opendir).grid(row=1, padx=10, pady=2)
		self.imgPathEntry = tki.Entry(self)
		self.imgPathEntry.grid(row=0, column=1)
		self.dirPathEntry = tki.Entry(self)
		self.dirPathEntry.grid(row=1, column=1)
		
		# 放映按钮：上一张图片 下一张图片
		self.lastImgBtn = tki.Button(self, text="Last Image", command=self.lastimg).grid(row=2, padx=10, pady=2)
		self.nextImgBtn = tki.Button(self, text="Next Image", command=self.nextimg).grid(row=3, padx=10, pady=2)
		
		# 保存按钮：保存框选好的图片
		self.saveBtn = tki.Button(self, text="Save", command=self.save).grid(row=4, padx=10, pady=2)
		
		# 放映标签：放映打开的图片
		firstPhoto_img = Image.open("totalblack.jpg")
		firstPhoto = ImageTk.PhotoImage(firstPhoto_img)
		
		self.panelLabel = tki.Label(self, image=firstPhoto)
		self.panelLabel.grid(row=0, column=2, rowspan=4, columnspan=4,
			sticky=tki.W+tki.E+tki.N+tki.S, padx=10, pady=10)
		self.panelLabel.configure(image=firstPhoto)
		self.panelLabel.image = firstPhoto
		
		
	def openimg(self):
		pass
		
	def opendir(self):
		dirpath = self.dirPathEntry.get()
		file_name=glob(dirpath+"/*png")
		
		for file in file_name:
			pic = sm.imread(file).astype(np.float32)
			pic = sm.imresize(pic, (400,300)).astype(np.float32)
			self.sample.append(pic)
		 
		self.sample = np.array(self.sample)
		
		# 显示第一张图片
		pic = self.sample[0,:,:,:]
		pic = np.reshape(pic,(400,300,3)).astype(np.uint8)
		image = Image.fromarray(pic)
		image = ImageTk.PhotoImage(image)
		self.panelLabel.configure(image=image)
		self.panelLabel.image = image
		
	def lastimg(self):
		pass
		
	def nextimg(self):
		pic = self.sample[1,:,:,:]
		pic = pic.astype(np.uint8)
		image = Image.fromarray(pic)
		image = ImageTk.PhotoImage(image)
		self.panelLabel.configure(image=image)
		self.panelLabel.image = image
		
	def save(self):
		pass
		
		
		
		
		
		