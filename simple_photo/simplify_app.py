from glob import glob
import argparse
import tkinter.messagebox as msgbox
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
		self.master.geometry("980x420")
		self.createWeight()
		
		self.sample = []
		self.listpos = 0
		self.switch_rta = False
		# 初始化展示平面 条件语句保证其不被重复初始化
		if self.panelLabel != None:
			self.panelLabel = self.panelLabel
		else:
			self.panelLabel = None
		
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
			sticky=tki.W+tki.E+tki.N+tki.S, padx=10, pady=10)#
		self.panelLabel.configure(image=firstPhoto)
		self.panelLabel.image = firstPhoto

		# 放置可选框标题

		self.BoxLabel = tki.Label(self, text="Box Labels",width=20,bg="white")
		self.BoxLabel.grid(row=0, column=6)
		
		# 放置可选项
		self.statuslist = tki.StringVar()
		
		slb = tki.Scrollbar(self)
		slb.grid(row=1, column=7, ipady=70, sticky=tki.W)
	
		self.statebox = tki.Listbox(
			self, 
			listvariable=self.statuslist,
			yscrollcommand=slb.set)
		self.statebox.insert(tki.END, "人类")
		self.statebox.insert(tki.END, "球类")
		self.statebox.bind("<Double-Button-1>", self.rtaswitch) # 使用双击关联事件 因为单击会捕捉选定的动作 导致选定动作被搁置
		self.statebox.grid(row=1, column=6)
		
		self.addentry = tki.Entry(self,width=8)
		self.addbtn = tki.Button(
			self,
			text="Add Status",
			command=self.addstatus
			)
		self.addbtn.grid(row=2, column=6, sticky=tki.W)
		self.addentry.grid(row=2, column=7, sticky=tki.W)

	def openimg(self):
		pass
		
	def opendir(self):
		self.sample = []
		if self.dirPathEntry.get() != None:
			self.listpos = 0
			dirpath = self.dirPathEntry.get()
			self.file_name=glob(dirpath+"/*png")
			
			for file in self.file_name:
				pic = sm.imread(file).astype(np.float32)
				pic = sm.imresize(pic, (300,400)).astype(np.float32)
				self.sample.append(pic)
			 
			self.sample = np.array(self.sample)
			# 显示第一张图片
			pic = self.sample[self.listpos]
			#pic = np.reshape(pic,(400,300,3)).astype(np.uint8)
			pic = pic.astype(np.uint8)
			image = Image.fromarray(pic)
			image = ImageTk.PhotoImage(image)
			self.panelLabel.bind("<Button-1>",self.rtastart)
			self.panelLabel.bind("<ButtonRelease-1>",self.rtaend)
			self.panelLabel.grid(row=0, column=2, rowspan=4, columnspan=4,
				sticky=tki.W+tki.E+tki.N+tki.S, padx=10, pady=10)
			self.panelLabel.configure(image=image)
			self.panelLabel.image = image
			
		else:
			msgbox.showwarning(title="[WARNING]",message="THE DIR PATH IS NOT FILLED IN!")
		
	def lastimg(self):
		if self.listpos > 0:
			self.listpos -= 1
			pic = self.sample[self.listpos]
			pic = pic.astype(np.uint8)
			image = Image.fromarray(pic)
			image = ImageTk.PhotoImage(image)
			if self.panelLabel != None:
				self.panelLabel.configure(image=image)
				self.panelLabel.image = image
			else:
				msgbox.showwarning(title="[WARNING]",message="NO RESOURSE!")
		else:
			msgbox.showwarning(title="[WARNING]",message="THIS IS THE FIRST FRAME!")
		
	def nextimg(self):
		the_last_frame = self.sample.shape[0]
		if self.listpos < the_last_frame:
			self.listpos += 1
			pic = self.sample[self.listpos]
			pic = pic.astype(np.uint8)
			image = Image.fromarray(pic)
			image = ImageTk.PhotoImage(image)
			if self.panelLabel != None:
				self.panelLabel.configure(image=image)
				self.panelLabel.image = image
			else:
				msgbox.showwarning(title="[WARNING]",message="NO RESOURSE!")
		else:
			msgbox.showwarning(title="[WARNING]",message="THIS IS THE LAST FRAME!")				
		
	def save(self):
		if self.panelLabel != None:
			file_name_split = self.file_name[self.listpos].split("\\", 1)
			pic_save = cv2.cvtColor(self.sample[self.listpos], cv2.COLOR_BGR2RGB)
			cv2.imwrite(file_name_split[0]+"/remix_"+file_name_split[1], pic_save)
			
		else:
			msgbox.showwarning(title="[WARNING]",message="NO RESOURSE!")
	
	def addstatus(self):
		if self.addentry.get() != None:
			self.statebox.insert(tki.END, self.addentry.get())
		
		else:
			msgbox.showwarning(title="[WARNING]",message="THE ENTRY IS NOT FILLED IN!")
		
	def rtaswitch(self,event):
		# 画框操作的开关 检测listbox变量的listvariable文本内容（self.statuslist.get()）
		# 如果listbox被按下 则listvariable内容（self.statuslist.get()）增加了listbox的的value 开关打开
		if self.statuslist.get() != None:
			self.switch_rta = True
			self.status=self.statebox.get(int(self.statebox.curselection()[0]))
			
		else:
			self.switch_rta = False
	
	def rtastart(self,event):
		# 读取鼠标落点
		self.startx = event.x
		self.starty = event.y
	
	def rtaend(self,event):
		if self.switch_rta == True:
			# 读取鼠标释放点
			self.endx = event.x
			self.endy = event.y
			# 从Image格式转化为OpenCV格式
			pic = self.sample[self.listpos]
			pic = pic.astype(np.uint8)
			image = Image.fromarray(pic)
			img_rect = cv2.cvtColor(np.asarray(image),
				cv2.COLOR_RGB2BGR)
			# 进行画矩形框操作
			print("[INFO] Start drawing frame")
			cv2.rectangle(img=img_rect,pt1=(self.startx,self.starty),
				pt2=(self.endx,self.endy),color=(0,255,0),thickness=1)
			# 从OpenCV格式转化为Image格式
			# 画框操作保留副本 即可保留多个框
			image = Image.fromarray(cv2.cvtColor(img_rect,cv2.COLOR_BGR2RGB))
			self.sample[self.listpos] = cv2.cvtColor(img_rect,cv2.COLOR_BGR2RGB)
			# 重新化为ImageTk格式
			image = ImageTk.PhotoImage(image)
			self.panelLabel.configure(image=image)
			self.panelLabel.image = image
			print("[INFO] finish drawing frame")
			print("[INFO] Write the information for the frame")
			file_name_split = self.file_name[self.listpos].split("\\", 1)
			with open(file_name_split[0]+"/Frame_infor.txt",'a') as f_msg:
				f_msg.write("{0}，{1}，{2}，{3}，{4}第{5}张\n".format(
					self.status,
					(self.startx,self.starty),
					self.endx-self.startx,
					self.endy-self.starty,
					self.dirPathEntry.get(),
					self.listpos+1)
					)
		else:
			msgbox.showwarning(title="[WARNING]",message="CATEGORY NOT SELECTED!")

		