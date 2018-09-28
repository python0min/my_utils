#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Datetime : 18-9-20 下午6:02
# @Author : min
# @Site : 
# @function : 记录下来,写在py文件里,方便搜索.


def util1():
    """
    一.python的set和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素.
    集合对象还支持union(并集), intersection(交集), difference(差集)和sysmmetric difference(对称差集)
    等数学运算.
    """
    # ======================交集=========================
    # 方法一:
    a = [2, 3, 4, 5]
    b = [2, 5, 8]
    tmp = [val for val in a if val in b]
    print tmp
    # [2, 5]

    # 方法二
    print list(set(a).intersection(set(b)))

    # =====================并集===========================
    print list(set(a).union(set(b)))

    # =====================差集===========================
    print list(set(b).difference(set(a)))  # b中有而a中没有的
    print list(set(a).difference(set(b)))  # a中有而b中没有的

    """======================运算符================================"""
    # 集合支持一系列标准操作，包括并集、交集、差集和对称差集，例如：

    t = set([1, 2, 3])
    s = set([3, 4, 5])

    print t | s  # t 和 s的并集

    print t & s  # t 和 s的交集

    print t - s  # 求差集（项在t中，但不在s中）

    print t ^ s  # 对称差集（项在t或s中，但不会同时出现在二者中）


def util2():
    """
    判断对象类型: 2种方法
                    方法一的效率更高
    :return:
    """
    import types
    # 方法一 ========================================================
    tmp_value = 1
    print isinstance(tmp_value, (types.FloatType, types.IntType))

    # 方法二=========================================================
    if type(tmp_value) in (types.FloatType, types.IntType):
        print 111


def util3():
    """
    补0;补零
        1.这个zfill看起来也就是zero fill的缩写吧，看一下如何使用
        2.数字补零

    :return:
    """
    # ===========================zfill补0===========================================
    v1 = "123"
    r1 = v1.zfill(5)

    # ===========================zfill也可以给负数补0=================================
    v2 = '-123'
    r2 = v2.zfill(5)
    # ===========================对于纯数字也可以通过格式化的方式来补0====================
    v3 = 123
    r3 = '%05d' % v3
    print r1, type(r1)
    print r2, type(r2)
    print r3, type(r3)


def util4():
    """
        简写python;一行python;

    :return:
    """
    print 1 if True else '0'
    a = [2, 3, 4, 5]
    b = [2, 5, 8]
    tmp = [val for val in a if val in b]
    print tmp


def util5():
    """
    numpy操作;
            这样的二维数组[
                        [64, 0], [128, 1], [256, 0]
                       ]
            转成[
                [64, 128, 256], [0, 1, 0]
               ]
    :return:
    """
    import numpy as np
    data_list = [[64, 0], [128, 1], [256, 0]]
    data_arr = np.array(data_list).T.tolist()
    print data_arr


def util6():
    """

    :return:
    """
    import datetime
    # 当月1号
    print datetime.date(datetime.date.today().year, datetime.date.today().month, 1)
    # 当月1号
    print datetime.date.today().replace(day=1)
    # 上月1号
    print (datetime.date.today().replace(day=1) - datetime.timedelta(1)).replace(day=1)


if __name__ == '__main__':
    util6()

