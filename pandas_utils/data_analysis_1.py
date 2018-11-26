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


def func1():
    # 餐别
    DealPeriod = {
        9: u"早餐",
        10: u"中餐",
        11: u"午餐",
    }
    # read_csv里常用的 names, sep, usecols, dtype, headers, nrows
    # names指文件中没有列名,如果第一行没有列,可以用这个; usecols这个可以用来获取指定列; sep用什么符号分割; nrows : int, default None
    header_user = ['AccNum', 'AccName', 'DepNum']
    df_his = pd.read_csv("csv_dir/ac_paymentbooks_his.csv", sep=',', usecols=[2, 3, 4, 6, 9])
    df_user = pd.read_csv("csv_dir/id_AccountsInfo.csv", sep=',', names=header_user)
    df_dealer = pd.read_csv("csv_dir/ac_Dealer.csv", sep=',', nrows=10, dtype={'DealerNum': np.int64, 'RecFlag': np.int32})
    # --------------------data type of columns: df_his.dtypes---------------------
    # print df_his.dtypes
    # --------------------对df_dealer的dtype运用-------------------------------------------
    # print df_dealer
    # print df_dealer.dtypes
    # --------------------indexes: df_his.index-----------------------------------
    # print df_his.index
    # --------------------columns: df_his.columns-----------------------------------
    # print df_his.columns
    # --------------------values: df_his.values-----------------------------------
    # print df_his.values
    # --------------------shape: df_his.shape-----------------------------------
    # print df_his.shape
    # --------------------对df_his进行where筛选-------------------------------------------
    df_his = df_his[(df_his['FeeNum'] == 100) & (df_his['DealPeriodNo'].isin([9, 10, 11]))]
    # print df_his


def func2():
    """
    不堆积的2种方法
    :return:
    """
    # 方法一
    df_his = pd.read_csv("csv_dir/ac_paymentbooks_his.csv", sep=',', usecols=[2, 3, 4, 6, 9])
    df_his = df_his[(df_his['FeeNum'] == 100) & (df_his['DealPeriodNo'].isin([9, 10, 11]))]
    df_his = df_his['MonDeal'].groupby([df_his['DealerNum'], df_his['StaNum'], df_his['DealPeriodNo']]).agg(
        ['count', 'sum'])

    fos = []
    print df_his.unstack().fillna(0)
    for d in df_his.to_records():
        fos.append(list(d))
    print "------------------------------------------------------------------------------------------------"
    # 方法二
    new_df = pd.DataFrame(data=fos, columns=['DealerNum', 'StaNum', 'DealPeriodNo', 'count', 'sum'])
    new_df['new_clo'] = new_df['DealerNum'].map(str) + '-' + new_df["StaNum"].map(str)
    new_df.drop(columns=['DealerNum', 'StaNum'], inplace=True)
    new_df = new_df.pivot(index='new_clo', columns='DealPeriodNo', values=['count', 'sum']).reset_index().fillna(0)
    print new_df


if __name__ == '__main__':
    func2()