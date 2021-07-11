# -*- coding: utf-8 -*-

"""
@File    : server.py
@Time    : 2021/7/26 22:59
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import aiohttp_jinja2
import jinja2

import config

from aiohttp import web
from aiomysql.sa import SAConnection
from aiomysql.sa.result import ResultProxy
from aiomysql.sa.transaction import Transaction

from db import with_db
from models import student

routes = web.RouteTableDef()


@routes.get('/')
@aiohttp_jinja2.template('index.html')
@with_db
async def index(req, db: SAConnection):
    res: ResultProxy = await db.execute(
        student.select()
    )
    students = await res.fetchall()
    return dict(
        title='学生管理系统',
        students=students,
    )


@routes.get('/add')
@routes.post('/add')
@aiohttp_jinja2.template('edit.html')
@with_db
async def add_student(req: web.Request, db: SAConnection):
    if req.method == 'POST':
        param = await req.post()
        name = param.get('name', '')
        age = param.get('age', '')
        if name and age:
            trans: Transaction = await db.begin()
            try:
                res: ResultProxy = await db.execute(
                    student.insert().values(
                        name=name,
                        age=age,
                    )
                )
                print(f'添加{res.rowcount}条学生数据')
            except Exception as e:
                print(e)
                await trans.rollback()
            else:
                await trans.commit()
            raise web.HTTPFound('/')
    return dict(
        title='添加学生',
    )


@routes.get(r'/edit/{id:\d+}', name='edit')
@routes.post(r'/edit/{id:\d+}')
@aiohttp_jinja2.template('edit.html')
@with_db
async def edit_student(req: web.Request, db: SAConnection):
    stu = None
    student_id = int(req.match_info.get('id', 0))

    if req.method == 'GET':
        res: ResultProxy = await db.execute(
            student.select().where(
                student.columns.id == student_id
            )
        )
        stu = await res.fetchone()
    elif req.method == 'POST':
        param = await req.post()
        name = param.get('name', '')
        age = param.get('age', '')
        if name and age:
            trans: Transaction = await db.begin()
            try:
                res: ResultProxy = await db.execute(
                    student.update().where(
                        student.columns.id == student_id
                    ).values(
                        name=name,
                        age=age,
                    )
                )
                print(f'编辑{res.rowcount}条学生数据')
            except Exception as e:
                print(e)
                await trans.rollback()
            else:
                await trans.commit()
        else:
            location = req.app.router['edit'].url_for(id=f'{student_id}')
            raise web.HTTPFound(location)

    if not stu:
        raise web.HTTPFound('/')

    return dict(
        title='编辑学生',
        student=stu
    )


@routes.get(r'/del/{id:\d+}')
@with_db
async def delete_student(req: web.Request, db: SAConnection):
    student_id = int(req.match_info.get('id', 0))
    if student_id != 0:
        trans: Transaction = await db.begin()
        try:
            print(student_id)
            res: ResultProxy = await db.execute(
                student.delete().where(
                    student.columns.id == student_id
                )
            )
            print(f'删除{res.rowcount}条学生数据')
        except Exception as e:
            print(e)
            await trans.rollback()
        else:
            await trans.commit()

    raise web.HTTPFound('/')


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    # 配置静态文件路径
    for m in config.STATIC_MAPPING:
        app.router.add_static(
            m['web_path'],
            m['directory'],
        )
    # 配置模板文件根目录
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(config.TEMPLATE_ROOT),
    )
    web.run_app(app, port=8000)
