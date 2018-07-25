#!/usr/bin/env python3
#  -*- endcoding=UTF-8 -*-
import time

from flask import request, session, url_for, json
from sqlalchemy import and_
from ansibleApi import runner

from opsGame import app, db
from flask import render_template
import commands, json

# 传入inventory路径
from opsGame.models import processMonitor,fileSystemMonitor, hosts

ansible = runner.ansibleRunner('/etc/ansible/Inventory/hosts')


# 主页
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/FileDo/', methods=['GET', 'POST'])
def fileDo():
    if request.method == "POST":
        jsonData = request.get_json()
        # print(jsonData)
        host = jsonData['host']
        module_name = jsonData['src']
        module_args = jsonData['dest']

        ansible.run(host, 'copy', 'src=' + module_name + ' ' + 'dest=' + module_args)
        # 结果
        result = ansible.get_result()
        # 成功
        succ = result['success']
        # 失败
        failed = result['failed']
        # 不可到达
        unreachable = result['unreachable']
        data = {}
        data['status'] = 'success'
        data['successHosts'] = list(result['success'].keys())
        data['failedHosts'] = list(result['failed'].keys())
        data['unreachableHosts'] = list(result['unreachable'].keys())
        data['hosts'] = {}
        if result['success']:
            for dict in result['success']:
                data['hosts'][dict] = result['success'][dict]
        if result['failed']:
            for dict in result['failed']:
                data['hosts'][dict] = result['failed'][dict]
        if result['unreachable']:
            for dict in result['unreachable']:
                data['hosts'][dict] = result['unreachable'][dict]
        return json.dumps(data)

    return render_template('filedo.html')


@app.route('/Monitor/', methods=['GET', 'POST'])
def monitor():
    return render_template('monitor.html')


@app.route('/Playbook/', methods=['GET', 'POST'])
def playbook():
    return render_template('playbook.html')


@app.route('/Shell/', methods=['GET', 'POST'])
def shell():
    return render_template('shell.html')


'''
    命令模式，返回json
    json：
    data[status]:success/failed 返回数据的json状态类型
    data[successHosts]:成功执行或者返回信息的ip列表
    data[failedHosts]：执行失败的主机ip列表
    data[unreachableHosts]：无法到达的主机ip列表
    data[host]：机器的具体状态列表，key中保存stdout_lines
    
'''


@app.route('/Command/', methods=["GET", "POST"])
def commandRun():
    if request.method == "POST":
        jsonData = request.get_json()
        print(jsonData)
        host = jsonData['host']
        module_name = jsonData['module_name']
        module_args = jsonData['module_args']

        ansible.run(host, module_name, module_args)
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
        data['successHosts'] = list(result['success'].keys())
        data['failedHosts'] = list(result['failed'].keys())
        data['unreachableHosts'] = list(result['unreachable'].keys())
        data['hosts'] = {}
        if result['success']:
            for dict in result['success']:
                data['hosts'][dict] = result['success'][dict]
        if result['failed']:
            for dict in result['failed']:
                data['hosts'][dict] = result['failed'][dict]
        if result['unreachable']:
            for dict in result['unreachable']:
                data['hosts'][dict] = result['unreachable'][dict]
        return json.dumps(data)
    return render_template('command.html')


@app.route('/ops/testPing', methods=['GET'])
def testPing():
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


# 进程监控 测试API
# 30s脚本传回json，若服务器无反馈3s持续向服务器发送
@app.route('/processPost/', methods=["GET", "POST"])
def processmonitor():
    if request.method == "POST":
        jsonData = request.get_json()
        print(jsonData)
        process = processMonitor.query.filter(and_(processMonitor.pName == jsonData['pName'], processMonitor.HostIP == jsonData['HostIP'])).first()
        tempHost = hosts.query.filter_by(hostIP=jsonData['HostIP']).first()
        group = tempHost.hostGroup
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if process is None:
            db.session.add(processMonitor(jsonData['pName'], jsonData['HostName'], jsonData['HostIP'], jsonData["CPU"],
                                          jsonData['Memory'], jsonData['RunTime'], jsonData["StartTime"],
                                          group, now))
        else:
            processMonitor.query.filter_by(pName=jsonData['pName'], HostIP=jsonData['HostIP']).update(
                {'CPU': jsonData["CPU"],
                 'Memory': jsonData['Memory'],
                 'RunTime': jsonData['RunTime'],
                 'Time': now})
    db.session.commit()
    return 'ok'


# 文件系统监控 测试API
# 300s监控脚本传回json，无反馈3s间断向服务器持续发送
@app.route('/FSMonitor/', methods=["GET", "POST"])
def fs():
    if request.method == "POST":
        jsonData = request.get_json()
        print(jsonData)
        fileSystem = fileSystemMonitor.query.filter(
            and_(fileSystemMonitor.FilePath == jsonData['FilePath'], fileSystemMonitor.HostIP == jsonData['HostIP'])).first()
        tempHost = hosts.query.filter_by(hostIP=jsonData['HostIP']).first()
        group = tempHost.hostGroup
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if fileSystem is None:
            db.session.add(fileSystemMonitor(jsonData['FilePath'], jsonData['HostIP'], jsonData['HostName'], jsonData['FS'],
                                          jsonData['Volume'], jsonData['Usage'], now, group))
        else:
            fileSystemMonitor.query.filter_by(FilePath=jsonData['FilePath'], HostIP=jsonData['HostIP']).update(
                {'Time': now,
                 'Usage': jsonData['Usage']})
    db.session.commit()
    return 'ok'
