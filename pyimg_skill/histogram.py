'''
cv2.calcHist
images：这是我们想要计算直方图的图像。把它包装成一个清单：[myImage]。
channels：索引列表，我们在其中指定要为其计算直方图的通道的索引。
要计算灰度图像的直方图，列表将是[0]。要计算所有三个红色，绿色和
蓝色通道的直方图，通道列表将是[0, 1, 2]。
mask：我还没有在这个博客中覆盖过遮蔽，但实际上，遮罩是一个与原始图像
具有相同形状的 uint8图像，其中忽略值为零的像素，值大于零的像素为
包括在直方图计算中。使用掩码允许我们仅计算图像的特定区域的直方图。现在，我们只使用None掩码的值  。
histSize：这是我们在计算直方图时要使用的位数。同样，这是一个列表，
我们正在为每个通道计算一个直方图。位的大小并非都必须相同。
以下是每个频道32个频段的示例：[32, 32, 32]。
range：可能的像素值范围。通常，这适用[0, 256]于每个通道，
但如果您使用RGB以外的颜色空间（例如HSV），则范围可能不同。
'''


# import the necessary packages
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
 
# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("image", image)
# convert the image to grayscale and create a histogram
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

# grab the image channels, initialize the tuple of colors,
# the figure and the flattened feature vector
chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
features = []
imglist = []
# loop over the image channels
for (chan, color) in zip(chans, colors):
	# create a histogram for the current channel and
	# concatenate the resulting histograms for each
	# channel
	imglist.append(chan)
	hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
	features.extend(hist)
 
	# plot the histogram
	plt.plot(hist, color = color)
	plt.xlim([0, 256])
plt.show()
cv2.imshow("1",imglist[0])
cv2.imshow("2",imglist[1])
cv2.imshow("3",imglist[2])
print ("flattened feature vector size: %d" % (np.array(features).flatten().shape))	
cv2.waitKey(0)