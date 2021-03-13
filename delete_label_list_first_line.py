# 删除label_list.txt文件的第一行无关数据，matlab我太笨了

import fileinput

txt_file = 'D:\\Research\\My_tamper_detect_dataset_generate\\dataset_tmp\\voc_dataset\\label_list.txt'

for line in fileinput.input(txt_file, inplace=1):
    if not fileinput.isfirstline():
        print(line.replace('\n', ''))
