from collections import deque
from imutils.video import VideoStream
import imutils
import cv2
import time
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())

greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
pts = deque(maxlen=args["buffer"])

if not args.get("video", False):
	vs = VideoStream(src=0).start()
	
else:
	vs = cv2.videoCapture(args["video"])
	
time.sleep(2.0)

while True:
	frame = vs.read()
	frame = cv2.flip(frame,1)
	#frame = np.uint8(np.clip((frame - 5), 0, 255)) #减小亮度的操作出现了bug
	
	frame = frame if not args.get("video", False) else frame[1]
	
	if frame is None:
		break
	
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11,11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=5)
	mask = cv2.dilate(mask, None, iterations=2)
	cv2.imshow("mask",mask)
	
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	center = None
	
	if len(cnts) > 0:
		
		c = max(cnts, key=cv2.contourArea)
		((x,y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"])) # 计算质心
		#center = (int(x),int(y))
		
		if radius > 20:
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(0,255,255), 2)
			cv2.circle(frame, center, 5, (0,0,255), -1) # -1为填充圆
			
	pts.appendleft(center) # 在if len(cnts) > 0外添加列表元素 是因为画线的时候要看当前帧和前一帧的center是否都不为None 若都不为None才执行画线 因此就算center为None也要添加进列表
	
	'''遍历质心画轨迹的逻辑很巧妙
	首先 pts是双向管列表 因为轨迹需要往前画
	因此新的帧往列表左边添加并且遍历时检测当前帧和后一帧 都不为None时画线 才能做到画出往前的轨迹
	并且使用往左添加可以避免前后两帧用 i 和 i+1 出现超出索引范围的问题
	并且在只检测到两个点时画出两点之间的连线 三个点时再遍历再画出两两之间的连线
	每多一帧 若检测到球 就更新一帧的画线 每一帧就重新用从前到后递减的粗细度来画线'''
	for i in range(1, len(pts)):
	
		if pts[i] is None or pts[i-1] is None:
			continue
		
		thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5) # 这个算式保证了越前面的帧厚度越小 直到趋于0后取整型 厚度就为0了 这就有了线的厚度越来越小直至没有
		cv2.line(frame, pts[i-1], pts[i], (0,0,255), thickness)
		
	cv2.imshow("Frame", frame)
	k = cv2.waitKey(1) & 0xFF
	
	if k == ord("q"):
		break
	
if not args.get("video", False):
	vs.stop()
			
else:
	vs.release()		
		
cv2.destroyAllWindows()		
		
		
		
		
		
		
		
