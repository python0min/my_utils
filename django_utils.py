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
    fileds = model_obj._meta.fields

    for i in fileds:
        print i.get_attname_column()[0]  # 数据库字段名
        print i.name  # field的名称
        print i.verbose_name  # 对应的中文名称


if __name__ == '__main__':
    dd_get_model_field()

