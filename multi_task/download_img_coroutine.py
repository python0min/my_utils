# -*- coding: utf-8 -*-
import requests
import gevent
import sys
from gevent import monkey
import os
import csv
# 如果是python3
if sys.version_info >= (3, 0):
    import urllib.request
else:
    import urllib

"""
使用多线程的方式下载图片
"""

monkey.patch_all()


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


def fetch(url):
    print("get: {}".format(url))
    response = requests.get(url).content
    return url, len(response)


def main():
    with open("read_csv/qi_niu_img.csv") as fr:
        reader = csv.reader(fr)
        data_list = list(reader)
    g_list = list()
    for url in data_list[1:5]:
        g = gevent.spawn(download, url)
        g_list.append(g)
    gevent.joinall(g_list)
    # for g in g_list:
    #     print(g.value)


if __name__ == '__main__':
    import time
    t1 = time.time()
    # export_qi_niu()
    main()
    t2 = time.time()
    print(t2 - t1)
