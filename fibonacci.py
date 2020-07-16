#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Datetime : 19-4-3 下午5:48
# @Author : min
# @Site : 
# @function :


class FibonacciIter(object):
    """
    用迭代器的方式实现斐波那契数列
    迭代器的优点，占用极小的空间去迭代
    """

    def __init__(self, all_num):
        self.a = 0
        self.b = 1
        self.current_num = 0
        self.all_num = all_num

    def __iter__(self):
        """
        有了这个方法就表示是一个迭代器
        :return:
        """
        return self

    def __next__(self):
        """
        :return:
        """
        if self.current_num < self.all_num:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return ret
        else:
            raise StopIteration


def fibo(all_num):
    """
    生成器实现斐波那契数列
    :param all_num:
    :return:
    """
    a = 0
    b = 1
    current_num = 0
    while current_num < all_num:
        yield a
        a, b = b, a + b
        current_num += 1


if __name__ == '__main__':
    fib = FibonacciIter(10)
    for num in fib:
        print(num)

    for f in fibo(10):
        print(f)