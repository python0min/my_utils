#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Datetime : 18-9-20 下午6:02
# @Author : min
# @Site : 
# @function : 记录下来,写在py文件里,方便搜索.
import time


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

    print t & s, " t 和 s的交集"  # t 和 s的交集

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
        一条/一行/
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
    当月1号;上月1号
    :return:
    """
    import datetime
    # 当月1号
    print datetime.date(datetime.date.today().year, datetime.date.today().month, 1)
    # 当月1号
    print datetime.date.today().replace(day=1)
    # 上月1号
    print (datetime.date.today().replace(day=1) - datetime.timedelta(1)).replace(day=1)


def get_merged_cells_value(sheet, row_index, col_index):
    """
    先判断给定的单元格，是否属于合并单元格；
    如果是合并单元格，就返回合并单元格的内容
    :return:
    """
    merged = sheet.merged_cells
    for (r_low, r_high, c_low, c_high) in merged:
        if r_low <= row_index < r_high:  # row_index >= r_low and row_index < r_high
            if c_low <= col_index < c_high:  # col_index >= c_low and col_index < c_high
                cell_value = sheet.cell_value(r_low, c_low)
                # print('该单元格[%d,%d]属于合并单元格，值为[%s]' % (row_index, col_index, cell_value))
                return cell_value
    return None


def util7(file_name, sheet_index=0):
    """
    读取excel文件并且将合并单元格的值赋给小单元格
    :param file_name:
    :param sheet_index:
    :return: 返回所有行的数据
    """
    # 打开文件
    import xlrd
    workbook = xlrd.open_workbook(file_name)
    # 获取所有sheet
    sheet_obj = workbook.sheet_by_index(sheet_index)  # sheet索引从0开始
    rows_num = sheet_obj.nrows  # 行数
    cols_num = sheet_obj.ncols  # 列数
    data_list = []
    materiel_code = sheet_obj.row_values(1)[1]  # 某一个单元格的值
    print materiel_code
    for r in range(1, rows_num):
        # 一行数据的实体类
        # entity_dict = {}
        entity_list = []
        for c in range(cols_num):
            cell_value = sheet_obj.row_values(r)[c]
            # print('第%d行第%d列的值：[%s]' % (r, c, sheet2.row_values(r)[c]))
            if cell_value is None or cell_value == '':
                cell_value = (get_merged_cells_value(sheet_obj, r, c))
            entity_list.append(cell_value)
        # print entity_list
        data_list.append(entity_list)
    return data_list


def util8(file_name, col_name_index=0, by_name=u'Sheet1'):
    import xlrd
    data = xlrd.open_workbook(file_name)
    # table = data.sheet_by_name(by_name)
    table = data.sheet_by_index(0)
    n_rows = table.nrows   # 行数
    # col_names = table.row_values(col_name_index)  # 某一行数据
    data_list = []
    for r in range(1, n_rows):
        row = table.row_values(r)
        data_list.append(row)
    return data_list


def util9():
    """
    某个月的第一天和最后一天
    :return:
    """
    import calendar as cal
    import datetime
    happened_time = '2017-05-02'
    start_time = datetime.datetime.strptime(happened_time, "%Y-%m-%d").replace(day=1)
    year, month = start_time.year, start_time.month
    d = cal.monthrange(year, month)
    end_time = start_time.replace(day=d[1], hour=23, minute=59, second=59)
    print start_time, end_time


def util10():
    # @function :3个方法,func1的效率最高,可以用于数据库查询分组
    """
      这样的结果  foo = [
              ('11013331', 'KAT'),
              ('9085267',  'NOT'),
              ('5238761',  'ETH'),
              ('5349618',  'ETH'),
              ('11788544', 'NOT'),
              ('962142',   'ETH'),
              ('7795297',  'ETH'),
              ('7341464',  'ETH'),
              ('9843236',  'KAT'),
              ('5594916',  'ETH'),
              ('1550003',  'ETH')
            ]
        想得到
        result = [
               {
                 type:'KAT',
                 items: ['11013331', '9843236']
               },
               {
                 type:'NOT',
                 items: ['9085267', '11788544']
               },
               {
                 type:'ETH',
                 items: ['5238761', '962142', '7795297', '7341464', '5594916', '1550003']
               }
             ]
    """

    def fun1():
        from collections import defaultdict
        foo = [('11013331', 'KAT'), ('9085267', 'NOT'), ('5238761', 'ETH'), ('5349618', 'ETH'), ('11788544', 'NOT'),
               ('962142', 'ETH'), ('7795297', 'ETH'), ('7341464', 'ETH'), ('9843236', 'KAT'), ('5594916', 'ETH'),
               ('1550003', 'ETH')]
        res = defaultdict(list)
        for v, k in foo:
            res[k].append(v)
        print res
        # list1 = [{'type': k, 'items': v} for k, v in res.items()]

    def fun2():
        from itertools import groupby
        from operator import itemgetter
        foo = [('11013331', 'KAT'), ('9085267', 'NOT'), ('5238761', 'ETH'), ('5349618', 'ETH'), ('11788544', 'NOT'),
               ('962142', 'ETH'), ('7795297', 'ETH'), ('7341464', 'ETH'), ('9843236', 'KAT'), ('5594916', 'ETH'),
               ('1550003', 'ETH')]
        sorted_foo = sorted(foo, key=itemgetter(1))
        groups = groupby(sorted_foo, key=itemgetter(1))
        # list2 = [{'type': k, 'items': [x[0] for x in v]} for k, v in groups]

    def func3():
        from collections import OrderedDict
        foo = [('11013331', 'KAT'), ('9085267', 'NOT'), ('5238761', 'ETH'), ('5349618', 'ETH'), ('11788544', 'NOT'),
               ('962142', 'ETH'), ('7795297', 'ETH'), ('7341464', 'ETH'), ('9843236', 'KAT'), ('5594916', 'ETH'),
               ('1550003', 'ETH')]
        res = OrderedDict()
        for v, k in foo:
            if k in res:
                res[k].append(v)
            else:
                res[k] = [v]
                # list3 = [{'type': k, 'items': v} for k, v in res.items()]
    fun1()
    fun2()
    func3()


def util11():
    """
    压缩文件夹  第一种写法
    : dir_name: 被文件夹目录
    : file_news:  压缩后的文件名
    :return:
    """
    import os
    import zipfile
    dir_name, file_news = '/data/projects/liu', '/data/projects/122.zip'
    try:
        file_list = []
        if os.path.isfile(dir_name):
            file_list.append(dir_name)
        else:
            for root, dirs, files in os.walk(dir_name):
                for name in files:
                    file_list.append(os.path.join(root, name))

        zf = zipfile.ZipFile(file_news, "w", zipfile.zlib.DEFLATED)
        for tar in file_list:
            arc_name = tar[len(dir_name):]
            # print arc_name
            zf.write(tar, arc_name)
        zf.close()
        return True
    except:
        import traceback
        traceback.print_exc()
        return False


def util12():
    """
    压缩文件夹 第二种写法,更简便
    : dir_name: 被文件夹目录
    : file_news:  压缩后的文件名
    :return:
    """
    import os
    import zipfile
    dir_name, file_news = '/data/projects/liu', '/data/projects/122.zip'
    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)  # 参数一：文件夹名
    for dir_path, dir_names, file_names in os.walk(dir_name):
        f_path = dir_path.replace(dir_name, '')  # 这一句很重要，不replace的话，就从根目录开始复制
        f_path = f_path and f_path + os.sep or ''  # 这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
        for filename in file_names:
            z.write(os.path.join(dir_path, filename), f_path + filename)
    z.close()


def util13():
    """
        获取某一年的每个周一的日期
    """
    import datetime
    t_now = datetime.datetime.now()
    now_year = t_now.year
    year_num = 2018
    # start_date 某年的1月1日
    start_date = datetime.datetime(year_num, 1, 1)
    # end_date 某年的12月31日
    end_date = datetime.datetime(year_num, 12, 31)
    # week_count 某年的1月1日所在的当前周数
    week_count = start_date.strftime("%W")
    if now_year == year_num:
        # total_count 如果是当前年份则是当前的周数
        total_count = int(t_now.strftime("%W")) - 1
    else:
        # 否则返回所有周的总数
        total_count = int(end_date.strftime("%W"))
    if week_count == '00':
        # diff为与下周一相差的天数, start_date则为某一年第一周第一个星期一的日期
        diff = 8 - start_date.isoweekday()
        start_date = start_date + datetime.timedelta(days=diff)
    count_date_dict = {}
    for i in range(1, total_count + 1):
        # 这里也可以返回时间戳
        temp = start_date.strftime('%Y-%m-%d %H:%M:%S')
        count_date_dict[i] = temp
        start_date += datetime.timedelta(days=7)
    print count_date_dict


def util14():
    """
    查找重复元素
    : list_a:
    :return:
    """
    list_a = [1, 2, 3, 3, 4, 4, 5, None, None]
    tem_set = set(list_a)
    b_list = []
    for item in tem_set:
        if list_a.count(item) > 1:
            b_list.append(item)
    return b_list


def expand_list(nested_list):
    """将多维的数组变成一维数组"""
    from sqlalchemy.engine.result import RowProxy
    for item in nested_list:
        if isinstance(item, (list, tuple, RowProxy)):
            for sub_item in expand_list(item):
                yield sub_item
        else:
            yield item


def list_count():
    """
    矩阵数组计数的几种方式
    :return:
    """
    import numpy as np
    from collections import Counter
    foo = [['0', '1', '1'],
           ['3', '0', '1'],
           ['1', '4', '1'],
           ['1', '0', '5']]*10000
    # **********************方式一*****************************
    # filter 这个方式过滤的方式来计数，缺点是只能统计一个纵列
    t1 = time.time()
    filter(lambda x: x[0] == '0', foo)
    t2 = time.time()
    print "1"*10, t2 - t1
    # **********************方式二*****************************
    foo_new = np.array(foo).T.tolist()
    Counter(foo_new[0])
    t3 = time.time()
    print "2"*10, t3 - t2
    # **********************方式三*****************************
    # 假定数组为a，可以先试用a == 某个数，转换为一个包含True或者False的数字，
    # 等于该树则为True，不等于则为False，True又可以当作1，False可以当作0，
    # 使用np.sum求和可以得到等于该数的总个数
    a = np.array(foo)
    # print(a)
    np.sum(a == '1', axis=1)  # 横列为‘1’的个数
    np.sum(a == '1', axis=0)  # 纵列为‘1’的个数
    np.sum(a == '1')  # 总共为‘1’的个数
    t4 = time.time()
    print "3"*10, t4 - t3


def date_to_stamp():
    """
        时间戳转datetime
        datetime转时间戳
        datetime格式化字符串
    :return:
    """
    import datetime
    # **********************字符串转datetime再转时间戳*****************************
    start_time = '2019-04-02 14:00:22'
    begin_date = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    begin_stamp = time.mktime(begin_date.timetuple())
    print begin_date, begin_stamp
    # **********************把datetime转成字符串*****************************
    t_now = datetime.datetime.now()
    now_str = t_now.strftime('%Y-%m-%d %H:%M:%S')
    print now_str
    # **********************把字符串转成datetime*****************************
    start_time = '2019-04-02 14:00:22'
    begin_date = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    print begin_date
    # **********************把时间戳转成字符串形式*****************************
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(begin_stamp))
    # **********************把时间戳转成datetime*****************************
    u = 1439111214.0  # unix时间戳
    t = datetime.datetime.fromtimestamp(u)
    print t

    st = time.localtime(1350816710.8050799)
    print st


def numpy_pad():
    """
    填充
    :return:
    """
    import numpy as np
    # --------------------------------------------------------------------------------------
    arr1D = np.array([[[1, 1, 2, 2, 3, 4], [1, 1, 2, 2, 3, 4], [1, 1, 2, 2, 3, 4]],
                  [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]],
                  [[1, 1, 2, 2, 3, 4], [1, 1, 2, 2, 3, 4], [1, 1, 2, 2, 3, 4]]])
    '''不同的填充方法'''
    print 'constant:  ', np.pad(arr1D, (2, 3), 'constant')
    print 'edge:  ', np.pad(arr1D, (2, 3), 'edge')
    print 'linear_ramp:  ' + str(np.pad(arr1D, (2, 3), 'linear_ramp'))
    print 'maximum:  ' + str(np.pad(arr1D, (2, 3), 'maximum'))
    print 'mean:  ' + str(np.pad(arr1D, (2, 3), 'mean'))
    print 'median:  ' + str(np.pad(arr1D, (2, 3), 'median'))
    print 'minimum:  ' + str(np.pad(arr1D, (2, 3), 'minimum'))
    print 'reflect:  ' + str(np.pad(arr1D, (2, 3), 'reflect'))
    print 'symmetric:  ' + str(np.pad(arr1D, (2, 3), 'symmetric'))
    print 'wrap:  ' + str(np.pad(arr1D, (2, 3), 'wrap'))


def list_pad():
    """
    数组填充
    2个一维数组,变成1个二维数组,2个数组长度可以不一样,不一样的情况补None
    方法二效率最高
    """
    a = [1, 2, 3, 19, 28, 38, 18, 999]
    b = [1, 3]
    c = [2, 5]
    t1 = time.time()
    # -----------------------方法一--------------------
    map(lambda *row: list(row), a, b)
    t2 = time.time()
    print t2 - t1
    # -----------------------方法二 - -------------------
    map(None, a, c)
    t3 = time.time()
    print t3 - t2
    # -----------------------方法二 - -------------------
    map(lambda x, y: [x, y], a, c)
    t4 = time.time()
    print t4 - t3


def compact():
    # 以下方法使用 fliter() 删除列表中的错误值（如：False, None, 0 和“”）
    list_1 = [0, 1, False, 2, None, 3, 'a', 's', 34, '', 38]
    list_2 = list(filter(bool, list_1))
    print list_2


def chunk():
    # 以下方法使用 range() 将列表lst分块为指定size进行分割
    lst, size = [1, 2, 3, 4, 5], 2
    lis_re = list(map(lambda x: lst[x * size:x * size + size], list(range(0, int(len(lst) / size)))))
    print lis_re


if __name__ == '__main__':
    pass
