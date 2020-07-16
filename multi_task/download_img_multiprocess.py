# -*- coding: utf-8 -*-
import os
import requests
import csv

import multiprocessing
import sys
# 如果是python3
if sys.version_info >= (3, 0):
    import urllib.request
else:
    import urllib
"""
使用多进程的方式下载图片
"""


def download(e):
    name = e[1] + "_" + str(e[0])
    for i, base_url in enumerate(e[2].split(',')):
        # 设置下载后存放的存储路径
        pic_file = os.path.join('{}/'.format(e[3]), name + "_" + str(i))
        print(type(pic_file))
        if not os.path.exists(pic_file):
            pic_dir = os.path.dirname(pic_file)
            if not os.path.exists(pic_dir):
                print('pic dir not exists. created:' + pic_dir)
                os.mkdir(pic_dir)
            if sys.version_info >= (3, 0):
                urllib.request.urlretrieve(base_url, pic_file)
            else:
                urllib.urlretrieve(base_url, pic_file)
        else:
            print('exists. skipped')


def main():
    # 1.创建进程池
    p = multiprocessing.Pool(4)
    # 3. csv文件顺序  sn_num,name,remark_pictures_text,unit_id
    with open("read_csv/qi_niu_img.csv") as fr:
        reader = csv.reader(fr)
        data_list = list(reader)
    # 2.向进程池中添加任务
    for d in data_list[1:10]:
        p.apply_async(download, args=(d,))
    p.close()
    p.join()


if __name__ == '__main__':
    import time
    t1 = time.time()
    # export_qi_niu()
    main()
    t2 = time.time()
    print(t2 - t1)




