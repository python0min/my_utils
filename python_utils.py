#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Datetime : 18-9-20 下午6:02
# @Author : min
# @Site : 
# @function : 平时经常网上搜索的功能,但由于经常会忘,所以还是记录下来,写在py文件


def util1():
    """
    一.python的set和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素.
    集合对象还支持union(并集), intersection(交集), difference(差集)和sysmmetric difference(对称差集)
    等数学运算.
    """


def util2():
    """
    判断对象类型:2种方法13332
                    isinstance的效率更高
    :return:
    """
    import types
    tmp_value = 1
    print isinstance(tmp_value, (types.FloatType, types.IntType))

    if type(tmp_value) in (types.FloatType, types.IntType):
        print 111


if __name__ == '__main__':
    util2()

