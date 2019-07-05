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
    """
    read_csv里常用的 names, sep, usecols, dtype, headers, nrows
    names指文件中没有列名,如果第一行没有列,可以用这个; usecols这个可以用来获取指定列; sep用什么符号分割; nrows : int, default None
    """
    header_user = ['AccNum', 'AccName', 'DepNum']
    df_his = pd.read_csv("csv_dir/ac_paymentbooks_his.csv", sep=',', usecols=[1, 2, 3, 4, 6, 9], nrows=20)
    df_user = pd.read_csv("csv_dir/id_AccountsInfo.csv", sep=',', names=header_user)
    df_dealer = pd.read_csv("csv_dir/ac_Dealer.csv", sep=',', nrows=10, dtype={'DealerNum': np.int64, 'RecFlag': np.int32})
    # --------------------data type of columns: df_his.dtypes-----------------------------------
    # print df_his.dtypes
    # --------------------对df_dealer的dtype运用--------------------------------------------------
    # print df_dealer
    # print df_dealer.dtypes
    # --------------------indexes: df_his.index--------------------------------------------------
    # print df_his.index
    # --------------------columns: df_his.columns------------------------------------------------
    # print df_his.columns
    # --------------------values: df_his.values--------------------------------------------------
    # print df_his.values
    # --------------------shape: df_his.shape----------------------------------------------------
    # print df_his.shape
    # =================================================select===========================================================
    print df_his
    # print df_his.loc[1:3, ['AccNum', 'FeeNum']]
    # print df_his.loc[1:3, 'AccNum': 'MonDeal']
    # print df_his.iloc[1:4, [0, 2]]
    # print df_his.iloc[1:4, 0: 2]
    # print df_his.at[3, 'AccNum']
    # print df_his.iat[3, 1]
    # print df_his.ix[1:3, [1, 2]]
    # print df_his.ix[1:3, ['AccNum', 'FeeNum']]
    # --------------------更简便的方式-------------------------------------------------------------
    # print df_his[1: 5]
    # print df_his[['AccNum', 'FeeNum']][1:5]
    # =================================================where============================================================
    # --------Pandas实现where filter，较为常用的办法为df[df[colunm] boolean expr]--------------------
    # print df_his[df_his['FeeNum'] == 35]
    # print df_his[df_his['AccNum'] > 2]
    # print df_his.query('FeeNum == 35')  # 换种写法
    # print df_his.query('AccNum > 2')
    # --------在where子句中常常会搭配and, or, in, not关键词，Pandas中也有对应的实现-----------------------
    # and
    # print df_his[(df_his['AccNum'] > 1) & (df_his['FeeNum'] == 35)]
    # or
    # print df_his[(df_his['AccNum'] > 1) | (df_his['FeeNum'] == 35)]
    # in
    # print df_his[df_his['AccNum'].isin([10053, 10265, 10222])]
    # not
    # print df_his[-(df_his['FeeNum'] == 35)]  # 或者  df_his.query('FeeNum != 35')
    # print df_his[-df_his['AccNum'].isin([10053, 10265, 10222])]
    # string function  这个没有实现
    # df_his = df_his[(-df_his['app'].isin(sys_app)) & (-df_his.app.str.contains('^微信\d+$'))]
    # print df_his.loc[df_his['FeeNum'] == 35, 'AccNum'].values
    # =================================================distinct=========================================================
    """包含参数：
                subset，为选定的列做distinct，默认为所有列；
                keep，值选项{'first', 'last', False}，保留重复元素中的第一个、最后一个，或全部删除；
                inplace ，默认为False，返回一个新的dataframe；若为True，则返回去重后的原dataframe  """
    # print df_his.drop_duplicates(subset=['FeeNum', 'MonDeal'], keep='first', inplace=False)
    # =================================================group============================================================
    """group一般会配合合计函数(Aggregate functions)使用,比如:count,avg,sum等.有count和size函数实现SQL的count："""
    # print df_his.groupby('FeeNum').size()
    # print df_his.groupby('FeeNum').count()
    print df_his['MonDeal'].groupby([df_his['DealerNum'], df_his['StaNum'], df_his['DealPeriodNo']]).agg(['count', 'sum'])
    # df_his.groupby('MonDeal').agg({'tip': np.max, 'total_bill': np.sum})
    # count(distinct **)
    # df_his.groupby('tip').agg({'sex': pd.Series.nunique})


def func2():
    """
    需求是统计: 商户信息和站点信息早餐.中餐.晚餐的消费金额,消费次数格式如下
              ---------------------------------------------------------------------------------
              | 商户  |  站点  |  合计   |       早餐       |       中餐        |      晚餐        |
              |      |       |        |--------------------------------------------------------
              |      |       |        | 消费金额 | 消费次数 | 消费金额 | 消费次数 | 消费金额 | 消费次数 |
              ---------------------------------------------------------------------------------
              | 餐厅  | 1号机 |  200   |   100  |    21    |    0   |    0    |   100  |   5    |
              ---------------------------------------------------------------------------------
              | 外卖  | 3号机 |  600   |   200  |    22    |   300  |    5    |   100  |   7    |
              ---------------------------------------------------------------------------------
              | 餐厅  | 5号机 |  300   |   100  |    12    |   100  |    2    |   100  |   6    |
              ---------------------------------------------------------------------------------
              | 合计  |      |  1100  |   400  |    55    |   400  |    7    |   300  |   18   |
              ---------------------------------------------------------------------------------
    不堆积的2种方法: 方法一比较好
    :return:
    """
    # 餐别
    DealPeriod = {
        9: u"早餐",
        10: u"中餐",
        11: u"午餐",
    }
    # 方法一
    df = pd.read_csv("csv_dir/ac_paymentbooks_his.csv", sep=',', usecols=[2, 3, 4, 6, 9])
    df = df[(df['FeeNum'] == 100) & (df['DealPeriodNo'].isin([9, 10, 11]))]
    print df.groupby('DealPeriodNo').count()
    df = df['MonDeal'].groupby([df['DealerNum'], df['StaNum'], df['DealPeriodNo']]).agg(['count', 'sum'])
    print df.unstack().fillna(0)
    print "------------------------------------------------------------------------------------------------"
    # 方法二
    fos = []
    for d in df.to_records():
        fos.append(list(d))
    new_df = pd.DataFrame(data=fos, columns=['DealerNum', 'StaNum', 'DealPeriodNo', 'count', 'sum'])
    new_df['new_clo'] = new_df['DealerNum'].map(str) + '-' + new_df["StaNum"].map(str)
    new_df.drop(columns=['DealerNum', 'StaNum'], inplace=True)
    new_df = new_df.pivot(index='new_clo', columns='DealPeriodNo', values=['count', 'sum']).reset_index().fillna(0)
    # print new_df


if __name__ == '__main__':
    func1()