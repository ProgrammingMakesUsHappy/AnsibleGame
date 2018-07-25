# -*- endcoding=UTF-8 -*-

from flask_admin import BaseView, expose
from sqlalchemy.orm import Session

from opsGame import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from opsGame.models import processMonitor, fileSystemMonitor, hosts



class MyView(BaseView):
    @expose('/', methods=['GET'])
    def index(self):
        return self.render('admin/getInfo.html')


class fileSystemView(ModelView):
    # 这三个变量定义管理员是否可以增删改，默认为True
    can_delete = False
    can_edit = False
    can_create = False
    # 这里是为了自定义显示的column名字
    column_labels = dict(
        # userName = u'用户名',

    )
    # 如果不想显示某些字段，可以重载这个变量
    column_exclude_list = (
        # 'userPwd'
        # 'table'
    )
    column_filters = ('FS', 'FilePath', 'Usage', 'HostName', 'HostIP', 'Volume', 'Time' )

class processMonitorViews(ModelView):
    # 这三个变量定义管理员是否可以增删改，默认为True
    can_delete = False
    can_edit = False
    can_create = False
    # 这里是为了自定义显示的column名字
    # column_labels = dict(
        #     # userName = u'用户名',
        #     jobfair_date = u'Date'
        #
        # )
    # 如果不想显示某些字段，可以重载这个变量
    # column_exclude_list = (
    #     'table',
    #     'jobfair_location'
    # )
    column_filters = ('pName', 'CPU', 'HostIP', 'HostName', 'RunTime', 'StartTime', 'Memory', 'Group',
                      'Time')


class hostsView(ModelView):
    # 这三个变量定义管理员是否可以增删改，默认为True
    can_delete = False
    can_edit = False
    can_create = False
    # 这里是为了自定义显示的column名字
    column_labels = dict(
        # userName = u'用户名',

    )
    # 如果不想显示某些字段，可以重载这个变量
    column_exclude_list = (
        # 'userPwd'
        # 'table'
    )
    column_filters = ('hostName', 'hostIP', 'hostGroup' )

admin = Admin(app, name=u'后台监控系统')

admin.add_view(processMonitorViews(processMonitor, db.session, name=u'进程监控'))
admin.add_view(fileSystemView(fileSystemMonitor, db.session, name=u"文件系统监控"))
admin.add_view(hostsView(hosts, db.session, name=u'主机列表'))