# import the necessary packages
from __future__ import print_function
import photoboothapp
from imutils.video import VideoStream
import argparse
import time

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
	help="path to output directory to store snapshots")
ap.add_argument("-p", "--picamera", type=int, default=-1,
	help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())
 
# 初始化视频流 允许摄像头预备
print("[INFO] warming up camera...")
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)
 
# 开启PhotoBoothApp 窗口循环
pba = photoboothapp.PhotoBoothApp(vs, args["output"])
pba.mainloop()