# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:36:48 2019

@author: Yann
"""
from keras.models import load_model
from processor import process_image
from keras import backend as K
import numpy as np
import cv2
import json
from collections import Counter 
  

from sklearn.metrics.pairwise import cosine_similarity

root = "./初赛A榜测试集/初赛A榜测试集/query_a/"

file_name = []
file = open("./初赛A榜测试集/初赛A榜测试集/query_a_list.txt",'r')

# 遍历文本文件的每一行，strip可以移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
for line in file.readlines():
    line = line.strip()
    k = line.split(' ')[0]
    k = k.split('/')[1]
    #v = line.split(' ')[1]
    file_name.append(k)

file.close()

###############################################################################
model = load_model('person_model')
layer_dense = K.function([model.layers[0].input], [model.layers[6].output])

def get_vec(x):
	image = process_image(root + x, (256, 128, 3))
	vec = layer_dense(image.reshape(1,256,128,3))[0]
	return vec
	
#image_2 = process_image("./初赛训练集/初赛训练集/train_set/963384410.png", (256, 128, 3))
#image_1 = np.array(image_1, dtype="float") / 255.0
#image_2 = np.array(image_2, dtype="float") / 255.0



dist_dict = {}


dist_map = np.zeros((1348,1348))

for i in range(0,1348):
	self = file_name[i]
	self_vec = get_vec(self)
	for j in range(i+1,1348):
		image = file_name[j]
		image_vec = get_vec(image)
		dist_map[i,j] = dist_map[j,i] = cosine_similarity(self_vec,image_vec)

for i in range(0,1348):
	line = dist_map[i]
	dist_arg = np.argsort(line)[::-1][0:200]
	#print(line[dist_arg])
	dist_dict[file_name[i]] = [file_name[x] for x in list(dist_arg)]
print("done")
json_vec = json.dumps(dist_dict, ensure_ascii=False)
#print(json_vec)

with open('answer.json', 'w') as f:
    f.write(json_vec)
	

# dictSortList = sorted( dist_dict.items(),key = lambda x:x[1],reverse = True)

# print(dictSortList)

#get_1_layer_output = K.function([model.layers[0].input, K.learning_phase()],
#						  [model.layers[0].output])
#pic_len = 1
#cv2.imshow("e",image_1)
# f1 = layer_dense(image_1.reshape(1,256,128,3))[0]
# img = np.squeeze(image_1.reshape(1,256,128,3))
# cv2.imshow("1",img)
# f2 = layer_dense(image_2.reshape(1,256,128,3))[0]  
# img = np.squeeze(image_2.reshape(1,256,128,3))
# cv2.imshow("2",img)      
# cv2.waitKey(0)

# cosine_dis2 = cosine_similarity(f1,f2)
# print(f1,"\n",f2,"\n",cosine_dis2)

#f1 = layer_dense([image_1])
#f2 = layer_dense([image_2])
#minus = f1-f2
#print(minus)









#from flashtorch.saliency import Backprop
#from flashtorch.utils import apply_transforms, load_image, visualize

########################################################################
# 声明一个空字典，来保存文本文件数据
#dict_temp = {}
#
## 打开文本文件
#file = open("./初赛训练集/初赛训练集/train_list.txt",'r')
#
## 遍历文本文件的每一行，strip可以移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
#for line in file.readlines():
#    line = line.strip()
#    k = line.split(' ')[0]
#    v = line.split(' ')[1]
#    dict_temp[k] = v
#
#file.close()
#######################################################################

#image = load_image("./初赛训练集/初赛训练集/train_set/00073233.png")
#input_ = apply_transforms(image)
#
#model = load_model('person_model')
#backprop = Backprop(model)
#
#target_class = dict_temp["00073233.png"]
#
#gradients = backprop.calculate_gradients(input_, target_class)
#max_guide_gradients = backprop.calculate_gradients(input_, target_class, take_max = True, guided = True)
#max_gradients = backprop.calculate_gradients(input_, target_class, take_max = True)
#
#visualize(input_, max_guide_gradients, max_gradients)

