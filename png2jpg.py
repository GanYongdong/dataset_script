import os
from pathlib import Path
import shutil
import numpy as np
import cv2
    

if __name__ == '__main__':
    ## 用户修改以下两个参数
    # png所在目录
    png_dir = '/media/ganyd/0C26A92126A90D30/Research/My_tamper_detect_dataset_generate/6dataset_irregular_png_06resize_3x3kernel_8class/rgbOut'
    jpg_dir = '/media/ganyd/0C26A92126A90D30/Research/My_tamper_detect_dataset_generate/6dataset_irregular_png_06resize_3x3kernel_8class/rgbOutJpg'
    ## 程序开始
    #获取目录下所有目录与文件名称
    fileNameList = os.listdir(png_dir)

    for i in range(len(fileNameList)):

        png_file = png_dir + '/' + fileNameList[i]
        png_img = cv2.imread(png_file,1)
        jpg_file = jpg_dir + '/' + fileNameList[i]
        jpg_file2 = jpg_file.replace('.png','.jpg')
        cv2.imwrite(jpg_file2,png_img,[int(cv2.IMWRITE_JPEG_QUALITY),100])
        # cv2.imwrite
        if i % 100 == 0:
            print(i, '/', len(fileNameList))