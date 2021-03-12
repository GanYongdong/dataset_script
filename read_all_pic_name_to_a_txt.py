import os
from pathlib import Path
import shutil
import numpy as np
import platform

## 用户修改以下两个参数
# txt所在目录
if platform.system().lower() == 'windows':
    print("windows")
    txt_dir = 'D:\\Research\\My_tamper_detect_dataset_generate\\dataset_tmp\\voc_label_xml'
elif platform.system().lower() == 'linux':
    print("linux")
    txt_dir = '/media/ganyd/0C26A92126A90D30/Research/My_tamper_detect_dataset_generate/6dataset_irregular_png_06resize_3x3kernel_8class/yolo_label_xml'

#获取目录下所有目录与文件名称
fileNameList = os.listdir(txt_dir)
txt_file = "D:\\Research\\My_tamper_detect_dataset_generate\\dataset_tmp\\voc_dataset\\ImageSets\\Main\\all_pic_name.txt"
file = open(txt_file, 'w').close() #清空txt
with open(txt_file, "a", encoding='utf-8') as f:  # 打开文件
    for i in range(len(fileNameList)):
        #txt_file = txt_dir + '/' + fileNameList[i]
        content = fileNameList[i].split('.',1)[0]  #去掉列表中每一个元素扩展名
        f.write(content)
        if i != len(fileNameList)-1:
            f.write("\n")
