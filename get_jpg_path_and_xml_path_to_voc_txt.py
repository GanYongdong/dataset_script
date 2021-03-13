# 获取图片路径和xml路径，放到同一个txt文件中

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
# 输出txt文件路径
dst_train_path = root_dir + 'voc_dataset\\ImageSets\\Main2\\train.txt'
dst_valid_path = root_dir + 'voc_dataset\\ImageSets\\Main2\\valid.txt'
dst_test_path = root_dir + 'voc_dataset\\ImageSets\\Main2\\test.txt'
dst_all_path = root_dir + 'voc_dataset\\ImageSets\\Main2\\all.txt'
dst_train_path2 = root_dir + 'voc_dataset\\ImageSets\\Main\\train.txt'
dst_valid_path2 = root_dir + 'voc_dataset\\ImageSets\\Main\\val.txt'
dst_test_path2 = root_dir + 'voc_dataset\\ImageSets\\Main\\test.txt'
# 比例
train_ratio = 0.9

# 程序开始
# 获取目录下所有目录与文件名称
fileNameList = os.listdir(src_xml_dir)
total_file_num = len(fileNameList)
train_file_num = round(total_file_num * train_ratio)
valid_file_num = total_file_num - train_file_num
# 清空几个文件
file1 = open(dst_train_path, 'w').close()
file2 = open(dst_valid_path, 'w').close()
file3 = open(dst_test_path, 'w').close()
file4 = open(dst_all_path, 'w').close()
file1 = open(dst_train_path, "a", encoding='utf-8')
file2 = open(dst_valid_path, "a", encoding='utf-8')
file3 = open(dst_test_path, "a", encoding='utf-8')
file4 = open(dst_all_path, "a", encoding='utf-8')
file11 = open(dst_train_path2, 'w').close()
file22 = open(dst_valid_path2, 'w').close()
file33 = open(dst_test_path2, 'w').close()
file11 = open(dst_train_path2, "a", encoding='utf-8')
file22 = open(dst_valid_path2, "a", encoding='utf-8')
file33 = open(dst_test_path2, "a", encoding='utf-8')


for i in range(len(fileNameList)):
    if i <= train_file_num:
        content = './JPEGImages/' + fileNameList[i] + ' ' + './Annotations/' + fileNameList[i] + '\n'
        content = content.replace('xml', 'jpg', 1)
        file1.write(content)
        file3.write(content)
        file4.write(content)
        content = fileNameList[i]
        content = content.replace('.xml', '\n', 1)
        file11.write(content)
        file33.write(content)
    else:
        content = './JPEGImages/' + fileNameList[i] + ' ' + './Annotations/' + fileNameList[i] + '\n'
        content = content.replace('xml', 'jpg', 1)
        file2.write(content)
        content = fileNameList[i]
        content = content.replace('.xml', '\n', 1)
        file22.write(content)
    if i % 50 == 0:
        print("%d \\ %d" % (i, total_file_num))

file1.close()
file2.close()
file3.close()
file4.close()
print("all finish!")
