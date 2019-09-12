# import the necessary packages
from __future__ import print_function
from PIL import Image
from PIL import ImageTk
import tkinter as tki
import tkinter.messagebox as msgbox
import threading
import datetime
import numpy as np
import time
import imutils
import cv2
import os
import pdb

		
class PhotoBoothApp(tki.Frame):
	def __init__(self, vs, outputPath, master = None):
		# Frame结构的初始化
		tki.Frame.__init__(self,master)
		self.pack()
		self.master.title("PyImageSearch PhotoBooth")# 窗口标题
		self.createWidgets()# 创建控件的函数
		
		# 存储视频流的对象和输出路径
		# 读取实时图像和线程停止项目的初始化
		self.vs = vs
		self.outputPath = outputPath
		self.frame = None
		self.stopEvent = None
		# 录制视频开关和录制视频时的读取视频流图像
		self.capswitch = False
		self.VideoFrame = None
		# 读取视频流线程初始化
		#self.thread = None
 
		# 初始化显示实时图像面板
		self.panel = None
		
		# 以帧读取视频的面板
		# 帧的存储列表和所在位置的初始化
		# 设置两个图片存储列表self.imagelist和self._PILImage
		# self.imagelist用于存储ImageTk格式图片；self._PILImage用于存储Image格式图片为了在OpenCV操作中用作和OpenCV格式的图片相互转化 相当于备用副本
		self.FrameLabel = None
		self.imagelist = None
		self._PILImage = None
		self.listpos = 0
		self.switch_rta = False
		self.startx = 0
		self.starty = 0
		self.endx = 0
		self.endy = 0
		
		self.stopEvent = threading.Event()# 创建一个事件管理标志表明用于结束进程 默认为False
		
		# 无需开启另一个线程 直接执行轮询函数
		self.videoLoop()
		
		# 当窗口关闭时的调用操作
		#self.root.wm_protocol("WM_DELETE_WINDOW", self.onClose)
		
	def createWidgets(self):
	
		#Frame1放置快照按键
		self.fm1 = tki.Frame(self)
		btn = tki.Button(self.fm1, text="Snapshot!",
			command=self.takeSnapshot)
		btn.pack(side="bottom", fill="both", expand="yes", padx=10,
			pady=10)
		self.fm1.pack(side="bottom")
		
		# Frame2放置录制视频按键
		self.fm2 = tki.Frame(self)
		
		self.fm2_top = tki.Frame(self.fm2)
		self.BtnVideo = tki.Button(self.fm2_top, text = 'Please enter video delays and start save video: '.title(),
			bg='#22C9C9',fg='white',command=self.savevideoswitch)
		self.BtnVideo.pack(side="left")
		self.DelaysEntry=tki.Entry(self.fm2_top,width=10)
		self.DelaysEntry.pack(side="left")
		self.fm2_top.pack(side="top")
		
		self.fm2_bottom = tki.Frame(self.fm2)
		self.VideoPathLabel = tki.Label(self.fm2_bottom,text="Specify your video storage path and filename: ".title(),bg='#FF4081',fg = 'white')
		self.VideoPathLabel.pack(side="left")
		self.VideoPathEntry = tki.Entry(self.fm2_bottom)
		self.VideoPathEntry.pack(side="left")
		self.fm2_bottom.pack(side="bottom",padx = 2)
		
		self.fm2.pack(side="bottom",padx = 2)
		
		# Frame3放置视频实时显示面板和开关摄像头按钮
		self.fm3 = tki.Frame(self)
		self.TurnOffBtn = tki.Button(self.fm3, text="Turn Off The Camera",
			bg='#FF4081',fg='white',command=self.onClose)
		self.TurnOffBtn.pack(side="top")
		self.TurnOnBtn = tki.Button(self.fm3, text="Turn On The Camera",
			bg='#22C9C9',fg = 'white',command = self.TurnOn)
		self.TurnOnBtn.pack(side="top")
		self.fm3.pack(side="left")
		
		# Frame4放置读取视频的各种控件
		self.fm4 = tki.Frame(self)
		self.fm4_top1 = tki.Frame(self.fm4)
		self.fm4_top2 = tki.Frame(self.fm4)
		
		self.VideoFromLabel = tki.Label(self.fm4_top1,
			text="enter the video path: ".title(),bg='#FF4081',fg='white')
		self.VideoFromLabel.pack(side="left")
		self.VideoFromEntry = tki.Entry(self.fm4_top1)
		self.VideoFromEntry.pack(side="left")
		self.fm4_top1.pack(side="top")
		self.PlayVideoBtn = tki.Button(self.fm4,text="Play The Video",
			bg='#22C9C9',fg='white',command=self.playvideo)
		self.PlayVideoBtn.pack(side="top")
		
		self.PlayPrevBtn = tki.Button(self.fm4_top2,
			text="the previous frame".title(),command=self.playlastframe)
		#self.PlayPrevBtn.bind("<Left>",func=self.playlastframe())	
		self.PlayPrevBtn.pack(side="left")
		
		self.PlayVideoFrame = tki.Button(self.fm4_top2,
			text="play video frame".title(),command=self.playvideoframe)
		self.PlayVideoFrame.pack(side="left")
		
		self.PlayNextBtn = tki.Button(self.fm4_top2,
			text="the next frame".title(),command=self.playnextframe)
		#self.PlayNextBtn.bind("<Right>",func=self.playnextframe())
		self.PlayNextBtn.pack(side="left")
		
		self.fm4_top2.pack(side="top")
		
		self.EndPlayBtn = tki.Button(self.fm4,text="End Play",
			bg='#FF4081',fg='white',command=self.endplay)
		self.EndPlayBtn.pack()

		self.fm4.pack(side="left")
		
		# Frame5放置图像标注模块
		self.fm5 = tki.Frame(self)
		
		# 放置可选框标题
		self.fm5_top = tki.Frame(self.fm5)
		self.BoxLabel = tki.Label(self.fm5_top, text="Box Labels",width=20,bg="white")
		self.BoxLabel.pack(side="top")
		self.fm5_top.pack(side="top",pady=10,padx=20)
		
		# 放置可选项
		self.statuslist = tki.StringVar()
		self.fm5_middle = tki.Frame(self.fm5)
		self.fm5_middle.pack(side="top")
		
		slb = tki.Scrollbar(self.fm5_middle)
		slb.pack(side="right", fill="y")
		
		self.fm5_middle.statebox = tki.Listbox(
			self.fm5_middle, 
			listvariable=self.statuslist,
			yscrollcommand=slb.set)
		self.fm5_middle.statebox.insert(tki.END, "人类")
		self.fm5_middle.statebox.insert(tki.END, "球类")
		self.fm5_middle.statebox.bind("<Double-Button-1>", self.rtaswitch) # 使用双击关联事件 因为单击会捕捉选定的动作 导致选定动作被搁置
		self.fm5_middle.statebox.pack(side="top")
		
		self.fm5_middle.addentry = tki.Entry(self.fm5_middle,width=8)
		self.fm5_middle.addbtn = tki.Button(
			self.fm5_middle,
			text="Add Status",
			command=self.addstatus
			)
		self.fm5_middle.addbtn.pack(side="right")
		self.fm5_middle.addentry.pack(side="right")

		self.fm5.pack(side="right")
		
	
	'''
	videoLoop函数逻辑：停止读取摄像头事件管理标志self.stopEvent若未设置为True
	则进行摄像头视频流self.vs的读取
	若实时显示面板self.panel尚未设置（初始值为None）
	则设置该面板为tkinter.Label 并将处理后的读取到的画面设置为Label图片
	若实时显示面板已设置过为Label（非None）
	则只需更新图片即可   这样就完成了实时显示摄像头画面
	'''
	def videoLoop(self):
		try:
			# 持续循环获取视频流图像直到需要停止
			if not self.stopEvent.is_set():
				# 从视频流中截取图像并调整其大小
				# 为有500像素的最大宽度
				self.frame = self.vs.read()
				self.frame = imutils.resize(self.frame, width=500)
		
				# OpenCV 按BGR颜色标准显示图像; 然而 PIL
				# 按RGB颜色标准显示图像, 因此我们需要去
				# 交换颜色频道, 并转换成PILImage和ImageTK格式
				# PILImage格式是PIL方法将numpy数组转化成图像时的默认格式 而ImageTk是为了符合Label设置图片需要的格式
				image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
				image = Image.fromarray(image)
				image = ImageTk.PhotoImage(image)
		
				# 如果实时显示面板为“空”，那么我们需要初始化它
				if self.panel is None:
					self.panel = tki.Label(self.fm3,image=image)
					self.panel.image = image
					self.panel.pack(side="left", padx=10, pady=10)
					self.fm3.pack(side="left")
		
				# 否则，仅更新面板
				else:
					self.panel.configure(image=image)
					self.panel.image = image

		except RuntimeError as e:
			print("[INFO] caught a RuntimeError")
            
		self.panel.after(10,self.videoLoop)
              
	def savevideo(self,VideoPath='C:/Users/杨扬/Pictures/output.avi',delays=float(10)):
		# 设置视频编码器格式和视频写入对象
		fourcc = cv2.VideoWriter_fourcc(*'XVID')
		out = cv2.VideoWriter(VideoPath, fourcc, 300.0, (640, 480))
		# 记入开启录制时间并打印录制日志
		starttime = time.time()
		print("[INFO] video recording...")
		# 检测录制开关
		# 循环截取视频流图像并写入视频对象
		# 到达指定视频延时或检测键盘输入“q”则停止录制
		while self.capswitch:
			self.VideoFrame =self.vs.read()
			out.write(self.VideoFrame)
			cv2.putText(self.VideoFrame,
                "Press Q to save and quit",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                (255, 0, 0), 1)#cv2.putText（视频画面，坐标，字体，大小，颜色，粗细）
			cv2.imshow('Video recording screen', self.VideoFrame)		
			if time.time()-starttime > delays or cv2.waitKey(1) & 0xFF == ord('q'):
				# cv2.waitKey(1) & 0xFF == ord('q')语句：
				# 因为 waitKey 函数返回键盘输入符号的ascii码
				print("[INFO] finish recording")
				break
				
		# 释放视频和关闭cv视频录制窗口
		out.release()
		cv2.destroyAllWindows()
		# 视频录制开关关闭
		self.capswitch = False
		
	def savevideoswitch(self):
		# 视频录制开关控制 调用录制函数
		self.capswitch = True
		self.savevideo(VideoPath=self.VideoPathEntry.get(),delays=float(self.DelaysEntry.get()))
		
	def playvideo(self):
		# 从硬盘路径获取视频
		# 读取视频图像并用cv窗口显示
		capture = cv2.VideoCapture(self.VideoFromEntry.get())
		if capture.isOpened():
			while True:
				ret,prev = capture.read()
				if ret == True:
					cv2.imshow("Video Playing",prev)
				else:
					print("[INFO] End Show")
					break
				#等待20ms 若用户按下Esc(ascii=27)则执行退出语句
				#若参数设为0 则无限等待
				if cv2.waitKey(20)==27:
					print("[INFO] End Show")
					break
		
		cv2.destroyAllWindows()	

	def playvideoframe(self):
		self.imagelist = []
		self._PILImage = []
		capture = cv2.VideoCapture(self.VideoFromEntry.get())
		if capture.isOpened():
			while True:
				ret,prev = capture.read()
				if ret == True:
					prev = imutils.resize(prev,width=400)
					image = cv2.cvtColor(prev,cv2.COLOR_BGR2RGB)
					image = Image.fromarray(image)
					self._PILImage.append(image) # 存储Image格式图片
					image = ImageTk.PhotoImage(image)
					self.imagelist.append(image) # 存储ImageTk格式图片
				else:
					break

		if self.FrameLabel == None:
			self.FrameLabel = tki.Label(self.fm4,image=self.imagelist[0])
			self.FrameLabel.image = self.imagelist[0]
			# 当展示面板出现时检测鼠标按下 获得画框的起落点
			self.FrameLabel.bind("<Button-1>",self.rtastart)
			self.FrameLabel.bind("<ButtonRelease-1>",self.rtaend)
			self.FrameLabel.pack(side="left")
			self.fm4.pack(side="left")
		else:
			self.FrameLabel.configure(image=self.imagelist[0])
			self.FrameLabel.image = self.imagelist[0]
			
	# 去除Label的图片还是没弄出来		
	def endplay(self):
		if self.FrameLabel != None:
			self.FrameLabel.configure(image=None)
			self.FrameLabel.image = None
			self.FrameLabel = None
		else:
			msgbox.showwarning(title="[WARNING]",message="FRAMELABEL IS NONE")
			
	def playnextframe(self):
		the_last_frame = len(self.imagelist)
		if self.listpos < the_last_frame:
			self.listpos += 1
			if self.FrameLabel != None:
				self.FrameLabel.configure(image=self.imagelist[self.listpos])
				self.FrameLabel.image = self.imagelist[self.listpos]
			else:
				msgbox.showwarning(title="[WARNING]",message="NO RESOURSE!")
		else:
			msgbox.showwarning(title="[WARNING]",message="THIS IS THE LAST FRAME!")
			
	def playlastframe(self):
		if self.listpos > 0:
			self.listpos -= 1
			if self.FrameLabel != None:
				self.FrameLabel.configure(image=self.imagelist[self.listpos])
				self.FrameLabel.image = self.imagelist[self.listpos]
			else:
				msgbox.showwarning(title="[WARNING]",message="NO RESOURSE!")
		else:
			msgbox.showwarning(title="[WARNING]",message="THIS IS THE FIRST FRAME!")
		
	def takeSnapshot(self):
		# 抓取当前时间用于构造文件名
		ts = datetime.datetime.now()
		filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
		p = os.path.sep.join((self.outputPath, filename))

		# 保存图像文件
		cv2.imwrite(p, self.frame.copy())
		print("[INFO] saved {}".format(filename))
        
	def onClose(self):
		# 设置结束进程事件为True 关闭视频流
		print("[INFO] closing...")
		self.stopEvent.set()
		# 若要更新Label里的图片，一定要把该Label本身和预备要换的图片都设成global
		# 而因为这里的Label为self.panel是类的一个属性 已经属于全局变量 所以此处只需设图片为global
		global image
		'''image = cv2.imread("totalblack.jpg")
		image = imutils.resize(image,width=500)
		cv2.imwrite("totalblack.jpg",image)
		image = ImageTk.PhotoImage(file="totalblack.jpg")
		self.panel.configure(image=image,text="Camera Off...",
			fg="white",compound="center")直接在Label上打印 text文本会无法去除'''
		# 注意：OpenCV读取、操作图片的实例变量不能和PIL操作实例是同一个
		# 因为其中涉及到颜色层顺序转变、从numpy数组转化为文字等转变
		image_cv = cv2.imread("totalblack.jpg")
		image_cv = imutils.resize(image_cv,width=500)
		image_cv = cv2.putText(image_cv,
			"Camera Off...",
			(200, 180), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.8,
			(255, 255, 255), 1)
			
		image = cv2.cvtColor(image_cv,cv2.COLOR_BGR2RGB)
		image = Image.fromarray(image)
		image = ImageTk.PhotoImage(image)
		self.panel.configure(image=image)
		self.panel.image = image
		
	def TurnOn(self):
		# 开启摄像头和时视频流
		print("[INFO] Turn On The Camera...")
		self.stopEvent.clear()
	
	def addstatus(self):
		if self.fm5_middle.addentry.get() != None:
			self.fm5_middle.statebox.insert(tki.END, self.fm5_middle.addentry.get())
		
		else:
			msgbox.showwarning(title="[WARNING]",message="THE ENTRY IS NOT FILLED IN!")
			
	def rtaswitch(self,event):
		# 画框操作的开关 检测单选按钮的variable文本内容（self.status.get()）
		# 如果单选按钮被按下 则variable文本内容（self.status.get()）变为单选按钮的value 开关打开
		if self.statuslist.get() != None:
			self.switch_rta = True
			self.status=self.fm5_middle.statebox.get(int(self.fm5_middle.statebox.curselection()[0]))
			
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
			img_rect = cv2.cvtColor(np.asarray(self._PILImage[self.listpos]),
				cv2.COLOR_RGB2BGR)
			# 进行画矩形框操作
			print("[INFO] Start drawing frame")
			cv2.rectangle(img=img_rect,pt1=(self.startx,self.starty),
				pt2=(self.endx,self.endy),color=(0,255,0),thickness=1)
			# 从OpenCV格式转化为Image格式
			# 画框操作保留副本 即可保留多个框
			self._PILImage[self.listpos] = Image.fromarray(cv2.cvtColor(img_rect,cv2.COLOR_BGR2RGB))
			self.imagelist[self.listpos] = Image.fromarray(cv2.cvtColor(img_rect,cv2.COLOR_BGR2RGB))
			# 重新化为ImageTk格式
			self.imagelist[self.listpos] = ImageTk.PhotoImage(self.imagelist[self.listpos])
			self.FrameLabel.configure(image=self.imagelist[self.listpos])
			self.FrameLabel.image = self.imagelist[self.listpos]
			print("[INFO] finish drawing frame")
			print("[INFO] Write the information for the frame")
			with open("Frame_infor.txt",'a') as f_msg:
				f_msg.write("{0}，{1}，{2}，{3}，{4}第{5}帧\n".format(
					self.status,
					(self.startx,self.starty),
					self.endx-self.startx,
					self.endy-self.starty,
					self.VideoFromEntry.get(),
					self.listpos)
					)
		else:
			msgbox.showwarning(title="[WARNING]",message="CATEGORY NOT SELECTED!")
			