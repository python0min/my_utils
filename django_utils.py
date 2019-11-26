#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Datetime : 18-9-20 下午6:02
# @Author : min
# @Site : 
# @function : 记录下来,写在py文件里,方便搜索.


def dd_get_model_field():
    """
    获取model的verbose_name和name的数据库的字段名
    # from mysite.manage.utils.import_util import dd_get_model_field
    """
    from django.apps import apps
    model_obj = apps.get_model('manage', 'monitor')  # 根据app_name,model_name获取对象
    filed_list = model_obj._meta.fields

    for i in filed_list:
        print i.get_attname_column()[0]  # 数据库字段名
        print i.name  # field的名称
        print i.verbose_name  # 对应的中文名称


def func1(app_label, model_name):
    """
        获取模型类的 第二种写法
    :param app_label:
    :param model_name:
    :return:
    """
    from django.contrib.contenttypes.models import ContentType
    content_type = ContentType.objects.get(app_label=app_label, model=model_name).first()


def dd_get_speed_query():
    """
    from mysite.manage.utils.import_util import dd_get_speed_query

    测试对象获取的速度: 结果是用"values"可以节省时间,比迭代对象快
    以30条的monitor表为例  速度如下:
    t2 - t1 0.286942005157
    t3 - t2 0.289361953735
    t4 - t3 0.442641019821
    t5 - t4 0.08580493927
    t6 - t5 0.119661092758
    t7 - t6 0.116844892502
    t8 - t7 0.080246925354
    t9 - t8 0.0833690166473
    t10 - t9 0.000324964523315
    t11 - t10 0.0799171924591
    :return:
    """
    import time
    from ..models.model_monitor import Monitor
    from collections import Counter
    from django.db.models import Count
    from pandas import DataFrame
    # from ..models.model_alarmdata import AlarmData
    from ...db_engine import query_all
    t1 = time.time()
    m_all = Monitor.objects.all()
    m1 = m_all.filter(branch_type=22).count()
    m2 = m_all.filter(branch_type=30).count()
    m3 = m_all.filter(branch_type=34).count()
    m4 = m_all.filter(branch_type=42).count()
    t2 = time.time()
    print "t2 - t1", t2 - t1
    m8 = Monitor.objects.filter(branch_type=22).count()
    m5 = Monitor.objects.filter(branch_type=30).count()
    m6 = Monitor.objects.filter(branch_type=34).count()
    m7 = Monitor.objects.filter(branch_type=42).count()
    t3 = time.time()
    print "t3 - t2", t3 - t2
    branch_list = []
    m9 = Monitor.objects.filter(branch_type__in=[22, 30, 34, 42])
    for ii in m9:
        branch_list.append(ii.branch_type)
    print Counter(branch_list)
    t4 = time.time()
    print "t4 - t3", t4 - t3
    sql = "select count(branch_type),branch_type from monitor where branch_type in (22, 30, 34, 42) GROUP BY branch_type;"
    c_data = query_all(sql)
    print c_data
    t5 = time.time()
    print "t5 - t4", t5 - t4
    sql2 = "select branch_type from monitor where branch_type in (22, 30, 34, 42)"
    c1_data = query_all(sql2)
    c1_data = map(lambda x: x[0], c1_data)
    print Counter(c1_data)
    t6 = time.time()
    print "t6 - t5", t6 - t5
    sql3 = "select branch_type from monitor where branch_type in (22, 30, 34, 42)"
    c3_data = query_all(sql3)
    df = DataFrame(data=c3_data, columns=['branch_type'])
    print df.groupby('branch_type').count()
    t7 = time.time()
    print "t7 - t6", t7 - t6
    m10 = Monitor.objects.filter(branch_type__in=[22, 30, 34, 42]).values('branch_type')
    c3_data = map(lambda x: x['branch_type'], m10)
    print Counter(c3_data)
    t8 = time.time()
    print "t8 - t7", t8 - t7
    m11 = Monitor.objects.filter(branch_type__in=[22, 30, 34, 42]).values('branch_type').annotate(dcount=Count('branch_type'))
    print m11
    t9 = time.time()
    print "t9 - t8", t9 - t8
    m12 = Monitor.objects.filter(branch_type__in=[22, 30, 34, 42])
    a = m12.query.group_by = ['branch_type']
    print a
    t10 = time.time()
    print "t10 - t9", t10 - t9
    branch_list1 = []
    m13 = Monitor.objects.filter(branch_type__in=[22, 30, 34, 42]).values('branch_type')
    for jj in m13:
        branch_list1.append(jj['branch_type'])
    print Counter(branch_list1)
    t11 = time.time()


if __name__ == '__main__':
    dd_get_model_field()

