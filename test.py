#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Datetime : 19-4-3 下午5:48
# @Author : min
# @Site : 
# @function :

from multiprocessing import Process
from threading import Thread
import os
import time


def work():
    # 计算密集型多进程效率高
    res = 1
    for i in range(1, 100000):
        res *= i
    return res


if __name__ == '__main__':
    from collections import defaultdict

    foo = [('11013331', 'KAT'), ('9085267', 'NOT'), ('5238761', 'ETH'), ('5349618', 'ETH'), ('11788544', 'NOT'),
           ('962142', 'ETH'), ('7795297', 'ETH'), ('7341464', 'ETH'), ('9843236', 'KAT'), ('5594916', 'ETH'),
           ('1550003', 'ETH')]
    res = defaultdict(list)
    for v, k in foo:
        res[k].append(v)
    print res