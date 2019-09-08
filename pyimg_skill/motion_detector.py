# 导入必要的包
from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2
import pdb
 
# 参数检查 检查输入视频流路径参数和最小区域参数
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())
 
# 视频流路径参数为空则读取摄像头
if args.get("video", None) is None:
	vs = VideoStream(src=0).start()
	time.sleep(2.0)
 
# 否则读取视频文件
else:
	vs = cv2.VideoCapture(args["video"])
 
# 初始化firstFrame用于保存视频的第一张画面用于动作捕捉的参考
firstFrame = None
# 轮询视频画面
while True:
	# 抓取当前画面 初始化视频状态 occupied/unoccupied 文本
	frame = vs.read()
	frame = frame if args.get("video", None) is None else frame[1]#如果未输入视频路径则是当前读取的图像
																  #若输入已有视频路径 则返回两个值 故frame为元组 其中frame[1]为图像
	text = "Unoccupied"
 
	# 如果视频画面未被抓取则到达了视频的最后
	if frame is None:
		break
 
	# 调整帧的大小至500 转成灰度图
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)#高斯模糊来平均21*21区域的像素强度来降噪
 
	# 初始化一次firstFrame
	if firstFrame is None:
		firstFrame = gray
		continue

	# 计算当前帧和第一帧之间的绝对差
	frameDelta = cv2.absdiff(firstFrame, gray)
	# 图像阈值处理 若图像差frameDelta超过阈值25 则用cv2.THRESH_BINARY方法将大于25的重置像素值为255(255是第三个参数 即白色的像素值)
	# 通过阈值处理和cv2.THRESH_BINARY方法 使得图像仅有黑白二值 称为二值图 cv2.findContours函数只处理二值图
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
	# [1]是因为cv2.threshold函数返回两个值							  
	# 第一个是阈值值 第二个是图像
	# 而[1]就表示返回的第二个值（即返回的图像）赋给thresh
	
	# cv2.dilate函数（膨胀操作）对阈值处理后的图像进行填充放大
	# 然后cv2.findContours函数 找到对阈值处理后的图像的轮廓线
	thresh = cv2.dilate(thresh, None, iterations=2)
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	'''
	cv2.findContours函数返回两个值（cv3返回三个值 且第一个是图像 后两个相同）
	分别是轮廓和层次结构numpy.ndarray
	故cnts的类型是一个元组 而imutils.grab_contours实则是基于OpenCV的一套工具 返回元组中的轮廓
	而轮廓实际上是点的集合
	故cnts[0]的类型是一个列表
	print(type(cnts)) # <class 'tuple'>
	print(type(cnts[0])) # <class 'list'>
	print(len(cnts)) # 2
	'''
	cnts = imutils.grab_contours(cnts)
 
	# 循环检查轮廓：两帧之间的绝对差可能会有很多微小的不同（如光线、阴影的变化）
	# 进而有许多微小变化的轮廓的产生并不是我们所需要的 因此需要通过轮询轮廓来过滤微小轮廓 捕捉真实动作
	for c in cnts:
		# if the contour is too small, ignore it
		if cv2.contourArea(c) < args["min_area"]:
			continue
 
		# 计算轮廓的边界框并在画面上显示出来
		# 更新画面显示文本
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		print(type(frame))
		pdb.set_trace()
		text = "Occupied"

	# 在画面左下角上显示时间
	cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

	# 显示画面（当前frame、画面差frameDelta、画面差加深thresh）
	cv2.imshow("Security Feed", frame)
	cv2.imshow("Thresh", thresh)
	cv2.imshow("Frame Delta", frameDelta)
	key = cv2.waitKey(1) & 0xFF
 
	# 按下‘q’停止循环
	if key == ord("q"):
		break

# 循环停止后停止摄像头工作（或释放视频流） 关闭所有窗口
vs.stop() if args.get("video", None) is None else vs.release()
cv2.destroyAllWindows()



		
