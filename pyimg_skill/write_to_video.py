#导入必要的库
from __future__ import print_function
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2

# 参数解析
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
	help="path to output video file")
ap.add_argument("-p", "--picamera", type=int, default=-1,
	help="whether or not the Raspberry Pi camera should be used")
ap.add_argument("-f", "--fps", type=int, default=20,
	help="FPS of output file")
ap.add_argument("-c", "--codec", type=str, default="MJPG",
	help="codec of output video")
args = vars(ap.parse_args())

# 初始化视频流并允许摄像头传感器预备
print("[INFO] warming up camera")
vs = VideoStream(usePiCamera=args["picamera"]>0).start()
time.sleep(2.0)

# 初始化视频编辑码、视频读入实例、画面大小以及零数组（numpy数组）
fourcc = cv2.VideoWriter_fourcc(*args["codec"])
writer = None
zeros = None

# 从视频流中轮询视频帧
while True:
	frame = vs.read()
	frame = imutils.resize(frame,width=300)
	
	if writer is None:
		(h,w) = frame.shape[:2]
		writer = cv2.VideoWriter(args["output"], fourcc, args["fps"],
			(w*2,h*2),True) # 注意VideoWriter中的画面大小顺序规定为（宽，高）
			#True则控制我们写入的是颜色帧 存储大小为两倍帧大小是为了放下四个不同通道的帧
		zeros = np.zeros((h,w),dtype="uint8")
	
	# 将画面分成它的RGB部分
	# cv2.split分离画面出来的R、G、B都是等大小的单通道图像 相当于单纯的把三个通道亮度信息分离
	# 而单通道图像只能根据R、G、B分别的亮度信息绘制出对应位置亮度的灰度图 因此使用等大小的零numpy数组用于拓展其余两个通道且通道值为零
	# 构造可以显示出RGB对应颜色的图像
	(B,G,R) = cv2.split(frame)
	R = cv2.merge([zeros, zeros, R])
	G = cv2.merge([zeros, G, zeros])
	B = cv2.merge([B, zeros, zeros])
	
	output = np.zeros((h*2, w*2, 3),dtype="uint8")
	output[0:h, 0:w] = frame
	output[0:h, w:w*2] = R
	output[h:h*2, 0:w] = B
	output[h:h*2, w:w*2] = G
		
	cv2.imshow("frame", frame)
	cv2.imshow("output",output)
	
	writer.write(output)
	
	key = cv2.waitKey(1)&0xFF
	if key == ord("q"):
		break
		
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
vs.stop()
writer.release()

		
		
		
		
		