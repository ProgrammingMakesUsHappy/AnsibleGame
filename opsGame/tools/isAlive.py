#!/usr/bin/env python3
#  -*- endcoding=UTF-8 -*-

import time
import datetime
from opsGame import db
from opsGame.models import hosts


'''
    使用isalive检验主机的在线状态

'''
nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
now = datetime.datetime.strptime(nowTime, '%Y-%m-%d %H:%M:%S')
hostList = hosts.query.all()
for host in hostList:
    tq = now - host.timestamp
    if tq.seconds > 300:
        hosts.query.filter_by(hostIP=host.hostIP).update({'status': 0})

db.session.commit()


