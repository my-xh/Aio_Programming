# -*- coding: utf-8 -*-

"""
@File    : models.py
@Time    : 2021/7/26 0:05
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import sqlalchemy

# 学生表
student = sqlalchemy.Table(
    'student', sqlalchemy.MetaData(),
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(255)),
    sqlalchemy.Column('age', sqlalchemy.Integer),
)
