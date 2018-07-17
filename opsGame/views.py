#!/usr/bin/env python3
#  -*- endcoding=UTF-8 -*-
import time

import flask
from flask import request, session, url_for, json
from sqlalchemy import and_
from werkzeug.utils import redirect
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.plugins.callback import CallbackBase

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
