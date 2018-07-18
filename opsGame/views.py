#!/usr/bin/env python3
#  -*- endcoding=UTF-8 -*-
import time

import flask
from flask import request, session, url_for, json
from sqlalchemy import and_
from werkzeug.utils import redirect
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader
from ansible.plugins.callback import CallbackBase

from ansibleApi import runner

from opsGame import app, db
# from opsGame.models import hostInfo
from flask import render_template
import commands, json


# 主页
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/cmd/', methods=['GET'])
def cmd():
    return "ok!路由测试成功"


@app.route('/ops/fileDo/', methods=['GET'])
def fileDo():
    return render_template('FileDo.html')


@app.route('/ops/testPing', methods=['GET'])
def testPing():

    # 传入inventory路径
    ansible = runner.ansibleRunner('/etc/ansible/inventory/hosts')
    # 获取服务器磁盘信息
    ansible.run('all', 'setup', "filter='ansible_mounts'")
    # 结果
    result = ansible.get_result()
    # 成功
    succ = result['success']
    # 失败
    failed = result['failed']
    # 不可到达
    unreachable = result['unreachable']

    print(succ)
    print(failed)
    print(unreachable)

    return "test ok!"