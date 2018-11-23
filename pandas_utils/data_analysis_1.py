#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Datetime : 18-11-22 上午10:36
# @Author : min
# @Site : 
# @function :
import pandas as pd
import xlwt
import time
import numpy as np


def set_style(name, height, bold=False):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    alignment = xlwt.Alignment()
    alignment.horz = 2  # 居中
    alignment.vert = 1  # 居中

    font.name = name  # 'Times New Roman'
    font.bold = bold

    font.color_index = 8
    font.height = height

    borders = xlwt.Borders()
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1

    style.font = font
    style.alignment = alignment
    style.borders = borders
    return style


def foo():
    # 餐别
    DealPeriod = {
        9: u"早餐",
        10: u"中餐",
        11: u"午餐",
    }
    # read_csv里常用的 names, sep, usecols, dtype, headers, nrows
    # names指文件中没有列名,如果第一行没有列,可以用这个; usecols这个可以用来获取指定列; sep用什么符号分割; nrows : int, default None
    header_user = ['AccNum', 'AccName', 'DepNum']
    df_1 = pd.read_csv("csv_dir/ac_paymentbooks_his.csv", sep=',', usecols=[2, 3, 4, 6, 9])
    df_2 = pd.read_csv("csv_dir/id_AccountsInfo.csv", sep=',', names=header_user)
    df_3 = pd.read_csv("csv_dir/ac_Dealer.csv", sep=',', nrows=10, dtype={'MonDeal': np.int32, 'DealPeriodNo': np.int32})
    # 对df_1进行筛选
    df_1 = df_1[(df_1['FeeNum'] == 100) & (df_1['DealPeriodNo'].isin([9, 10, 11]))]
    print df_1
    df_1 = df_1['MonDeal'].groupby([df_1['DealerNum'], df_1['StaNum'], df_1['DealPeriodNo']]).agg(['count', 'sum'])
    # print df_1

    # df.loc[df['A'] == 'foo']   df[df['A'] == 'foo']
    t1 = time.time()
    # a = df.loc[df['DealerNum'] == 100]
    t2 = time.time()
    # print t2 - t1

    # t3 = time.time()
    # print t3 - t2
    # df = pd.DataFrame(consume_data)
    # df_new = df[3].groupby([df[0], df[1], df[2]]).agg(['count', 'sum'])
    # fos = []
    # print df_new.unstack()
    # for d in df_new.to_records():
    #     fos.append(list(d))
    # new_df = pd.DataFrame(data=fos, columns=['DealerNum', 'StaNum', 'DealPeriodNo', 'count', 'sum'])
    # new_df['new_clo'] = new_df['DealerNum'].map(str) + '-' + new_df["StaNum"].map(str)
    # new_df.drop(columns=['DealerNum', 'StaNum'], inplace=True)
    #
    # new_df = new_df.pivot(index='new_clo', columns='DealPeriodNo', values=['count', 'sum']).reset_index().fillna(0)
    # print new_df



if __name__ == '__main__':
    foo()