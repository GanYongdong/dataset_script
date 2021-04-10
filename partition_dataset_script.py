## 划分数据集
## ganyongdong

import os
from pathlib import Path
import shutil
import random

def mod(a, b):    
    c = a // b
    r = a - c * b
    return r

def delte_last_line(file_name):
    # 按行读入，删除最后一行
    file_old = open(file_name, 'r', encoding="utf-8")
    lines = [i for i in file_old]
    del lines[-1]
    file_old.close()
    # 再覆盖写入
    file_new = open(file_name, 'w', encoding="utf-8")
    file_new .write(''.join(lines))
    file_new .close()

if __name__ == '__main__':
    #源图片所在目录
    pic_dir = os.getcwd() + '/JPEGImages'
    #生成txt所在目录
    txt_dir = os.getcwd() + '/ImageSets/Main/'
    #生成txt路径名
    train_txt_path = txt_dir + 'train.txt'
    val_txt_path = txt_dir + 'val.txt'
    test_txt_path = txt_dir + 'test.txt'
    trainval_txt_path = txt_dir + 'trainval.txt'

    #获取目录下所有目录与文件名称
    fileNameList = os.listdir(pic_dir)
    total_num = len(fileNameList)
    print('图片个数：',len(fileNameList))
    #划分比例，占所有图像的比例，三个不交叉。trainval由train和val合并形成，不需要指定
    train_rate = 0.4
    val_rate = 0.4
    test_rate = 0.2

    train_cnt = 0
    val_cnt = 0
    test_cnt = 0

    #打乱文件列表顺序
    random.shuffle(fileNameList)

    f1 = open(train_txt_path, "w")
    f2 = open(val_txt_path, "w")
    f3 = open(test_txt_path, "w")
    f4 = open(trainval_txt_path, "w")

    for i in range(len(fileNameList)):
        name_str = fileNameList[i].replace('.png','');
        if train_cnt < train_rate*total_num:
            train_cnt = train_cnt + 1
            if train_cnt != 1:
                f1.write('\n'+name_str)
            else:
                f1.write(name_str)
        elif val_cnt < val_rate*total_num:
            val_cnt = val_cnt + 1
            if val_cnt != 1:
                f2.write('\n'+name_str)
                f4.write('\n'+name_str)
            else:
                f2.write(name_str)
                f4.write(name_str)
        elif test_cnt < test_rate*total_num:
            test_cnt = test_cnt + 1
            if test_cnt != 1:
                f3.write('\n'+name_str)
            else:
                f3.write(name_str)
        if mod(i,1000)==0:
            print(i,'/',total_num)

    f1.close()
    f2.close()
    f3.close()
    f4.close()

    ##打印显示
    print('finish\n')
