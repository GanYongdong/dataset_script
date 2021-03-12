# 统计各类回归框的数量

import os
from pathlib import Path
import shutil
import numpy as np

# 用户修改以下两个参数
# txt所在目录
txt_dir = 'D:\\Research\\My_tamper_detect_dataset_generate\\5dataset_irregular_png_06resize_3x3kernel_addSharp\\yolo_label_txt'
# 总共有多少个类别
class_num = 6

# 程序开始
# 获取目录下所有目录与文件名称
fileNameList = os.listdir(txt_dir)

# 类别数量
classCount = np.zeros(class_num + 1)

for i in range(len(fileNameList)):

    txt_file = txt_dir + '/' + fileNameList[i]
    with open(txt_file, "r") as f:  # 打开文件
        for line in f.readlines():
            strList = line.split(' ')  # 空格划分
            classLabel = int(strList[0])
            classCount[classLabel] = classCount[classLabel] + 1

# 统计所有回归框总数
for i in range(len(classCount)):
    classCount[0] = classCount[0] + classCount[i]

# 计算各类别所占比例
classCountRate = np.zeros(class_num + 1)
for i in range(len(classCountRate)):
    classCountRate[i] = classCount[i] / classCount[0]

# 打印显示
for i in range(len(classCount)):
    if i == 0:
        print("总数量:\t%d\t%.3f" % (classCount[i], classCountRate[i]))
    else:
        print("第%d类:\t%d\t%.3f" % (i, classCount[i], classCountRate[i]))
