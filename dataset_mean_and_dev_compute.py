import numpy as np
import cv2
import random
from tqdm import *
import os
 
# calculate means and std
train_txt_path = '/home/ganyd/Research/SSD_defect/datasets/VOC2007/ImageSets/Main/train.txt'
 
CNum = 2000   # 挑选多少图片进行计算
 
img_h, img_w = 300, 300
imgs = np.zeros([img_w, img_h, 3, 1])
means, stdevs = [], []
 
with open(train_txt_path, 'r') as f:
  lines = f.readlines()
  random.shuffle(lines)  # shuffle , 随机挑选图片
 
#   for i in tqdm_notebook(range(CNum)):
all_num = len(lines)
for i in range(len(lines)):
    print("i=",i)
    img_path = os.path.join('/home/ganyd/Research/SSD_defect/datasets/VOC2007/JPEGImages', lines[i].rstrip().split()[0])
    #print("img_path",img_path)
    img_path = img_path + '.jpg'
    img = cv2.imread(img_path)
 
    img = cv2.resize(img, (img_h, img_w))
    #cv2.imshow('e', img)
    #cv2.waitKey(0)
    img = img[:, :, :, np.newaxis]
 
    imgs = np.concatenate((imgs, img), axis=3)
 
 
imgs = imgs.astype(np.float32)/255.
# imgs = imgs.astype(np.float32)
 
for i in (range(3)):
  pixels = imgs[:,:,i,:].ravel() # 拉成一行
  means.append(np.mean(pixels))
  stdevs.append(np.std(pixels))
 
# cv2 读取的图像格式为BGR，PIL/Skimage读取到的都是RGB不用转
means.reverse() # BGR --> RGB
stdevs.reverse()
 
print("normMean = {}".format(means))
print("normStd = {}".format(stdevs))
print('transforms.Normalize(normMean = {}, normStd = {})'.format(means, stdevs))
