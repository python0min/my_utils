# -*- coding: utf-8 -*-
import os
import csv
import threading
import time
import sys
# 如果是python3
if sys.version_info >= (3, 0):
    import urllib.request
else:
    import urllib
"""
使用多线程的方式下载图片
"""

threadLock = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, target):
        threading.Thread.__init__(self)
        self.threadId = thread_id
        self.name = name
        self.target = target

    def run(self):
        print(u"开始线程:", self.name)
        # 获得锁，成功获得锁定后返回 True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回 False
        # 循环:
        while True:
            try:
                threadLock.acquire()
                # 获得下一个值:
                x = next(self.target)
                # print("%s : %s" % (self.name, x), type(x))
                # 释放锁
                threadLock.release()
                download(x)
            except StopIteration:
                # 遇到StopIteration就退出循环
                threadLock.release()
                break

    def __del__(self):
        print(self.name, u"线程结束！")


def download(e):
    name = e[1] + "_" + str(e[0])
    for i, base_url in enumerate(e[2].split(',')):
        # 设置下载后存放的存储路径
        pic_file = os.path.join('{}/'.format(e[3]), name + "_" + str(i))
        # print(pic_file)
        if not os.path.exists(pic_file):
            pic_dir = os.path.dirname(pic_file)
            print(pic_dir)
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
    with open("read_csv/qi_niu_img.csv") as fr:
        reader = csv.reader(fr)
        data_list = list(reader)[1:10]
    it = iter(data_list)

    threads = []
    # 创建新线程
    for i in range(10):
        thread = MyThread(i, "Thread-%d" % i, it)
        # 添加线程到线程列表
        threads.append(thread)
    for th in threads:
        # 开启新线程
        th.start()
    for t in threads:
        # 等待所有线程完成
        t.join()
    print(u"主进程结束！")


if __name__ == '__main__':
    t1 = time.time()
    main()
    t2 = time.time()
    print(t2 - t1)





