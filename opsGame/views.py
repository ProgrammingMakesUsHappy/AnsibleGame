# -*- endcoding=UTF-8 -*-
import time

import flask
from flask import request, session, url_for, json
from sqlalchemy import and_
from werkzeug.utils import redirect
from ansible.inventory import Inventory
from ansible.playbook import PlayBook
from ansible import callbacks

from opsGame import app, db
#from opsGame.models import hostInfo
from flask import render_template
import ansible.runner
import commands, json

# 主页
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/cmd', methods=['GET'])
def cmd():
    return "ok!"
