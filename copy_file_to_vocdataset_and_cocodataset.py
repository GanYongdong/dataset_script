# 复制图片和标签文件到 voc dataset 和 coco dataset

import os
from pathlib import Path
import shutil
import numpy as np

# 用户修改以下两个参数
# 工作目录
root_dir = 'D:\\Research\\My_tamper_detect_dataset_generate\\dataset_tmp\\'
# 源xml所在目录
src_xml_dir = root_dir + 'voc_label_xml\\'
# 源图片所在目录
src_jpg_dir = root_dir + 'rgbOutJpg\\'
# 目的图片路径
dst_jpg_dir1 = root_dir + 'coco_dataset\\images\\'
dst_jpg_dir2 = root_dir + 'voc_dataset\\JPEGImages\\'
# 目的xml路径
dst_xml_dir = root_dir + 'voc_dataset\\Annotations\\'

# 程序开始
# 获取目录下所有目录与文件名称
fileNameList = os.listdir(src_xml_dir)
total_file_num = len(fileNameList)

for i in range(len(fileNameList)):
    # 源xml所在目录
    src_xml_file_path = src_xml_dir + fileNameList[i]
    # 目的xml路径
    dst_xml_file_path = dst_xml_dir + fileNameList[i]
    shutil.copyfile(src_xml_file_path, dst_xml_file_path)
    # 源图片所在目录
    src_jpg_file_path = src_jpg_dir + fileNameList[i]
    src_jpg_file_path = src_jpg_file_path.replace("xml", "jpg")
    # 目的图片路径
    dst_jpg_file_path1 = dst_jpg_dir1 + fileNameList[i]
    dst_jpg_file_path1 = dst_jpg_file_path1.replace("xml", "jpg")
    dst_jpg_file_path2 = dst_jpg_dir2 + fileNameList[i]
    dst_jpg_file_path2 = dst_jpg_file_path2.replace("xml", "jpg")
    shutil.copyfile(src_jpg_file_path, dst_jpg_file_path1)
    shutil.copyfile(src_jpg_file_path, dst_jpg_file_path2)

    if i % 50 == 0:
        print("%d \\ %d" % (i, total_file_num))
print("all finish!")
