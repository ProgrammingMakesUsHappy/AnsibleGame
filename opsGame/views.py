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

# 传入inventory路径
ansible = runner.ansibleRunner('/etc/ansible/inventory/hosts')


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


'''
    命令模式，返回json
    json：
    data[status]:success/failed 返回数据的json状态类型
    data[successHosts]:成功执行或者返回信息的ip列表
    data[failedHosts]：执行失败的主机ip列表
    data[unreachableHosts]：无法到达的主机ip列表
    data[host]：机器的具体状态列表，key中保存stdout_lines
    
'''
@app.route('/command/', methods=["GET"])
def commandPage():
    return render_template('command.html')


@app.route('/command/', methods=["GET", "POST"])
def commandRun():
    if request.method=="POST":
        jsonData = request.get_json()
        print(jsonData)
        host = jsonData['host']
        module_name = jsonData['module_name']
        module_args = jsonData['module_args']

        ansible.run(host, module_name,module_args)
        # 结果
        result = ansible.get_result()
        # 成功
        succ = result['success']
        # 失败
        failed = result['failed']
        # 不可到达
        unreachable = result['unreachable']
        # print(succ)
        # print(failed)
        # # print(unreachable)
        data = {}
        data['status'] = 'success'
        data['successHosts'] = result['success'].keys()
        data['failedHosts'] = result['failed'].keys()
        data['unreachableHosts'] = result['unreachable'].keys()
        data['hosts'] = {}
        if result['success']:
            for dict in result['success']:
                data['hosts'][dict] = result['success'][dict]
        if result['failed']:
            for dict in result['failded']:
                data['hosts'][dict] = result['failed'][dict]
        if result['unreachable']:
            for dict in result['unreachable']:
                data['hosts'][dict] = result['unreachable'][dict]
            # print(result['unreachable'][dict])
        print(data)
        return json.dumps(data)


@app.route('/ops/testPing', methods=['GET'])
def testPing():

    # 传入inventory路径
    # ansible = runner.ansibleRunner('/etc/ansible/inventory/hosts')

    # 获取服务器磁盘信息
    # ansible.run('all', 'setup', "filter='ansible_mounts'")
    ansible.run('all', 'command', 'ping 192.168.14.131 -c 5')
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