# -*- endcoding=UTF-8 -*-

from flask_admin import BaseView, expose
from sqlalchemy.orm import Session

from opsGame import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from opsGame.models import processMonitor, fileSystemMonitor



class MyView(BaseView):
    @expose('/', methods=['GET'])
    def index(self):
        return self.render('admin/getInfo.html')


class UserView(ModelView):
    # 这三个变量定义管理员是否可以增删改，默认为True
    can_delete = True
    can_edit = True
    can_create = True
    # 这里是为了自定义显示的column名字
    column_labels = dict(
        # userName = u'用户名',

    )
    # 如果不想显示某些字段，可以重载这个变量
    column_exclude_list = (
        'userPwd'
        'table'
    )
    column_filters = ('id','school')

class processMonitorViews(ModelView):
    # 这三个变量定义管理员是否可以增删改，默认为True
    can_delete = True
    can_edit = True
    can_create = True
    # 这里是为了自定义显示的column名字
    column_labels = dict(
        # userName = u'用户名',
        jobfair_date = u'Date'

    )
    # 如果不想显示某些字段，可以重载这个变量
    # column_exclude_list = (
    #     'table',
    #     'jobfair_location'
    # )


admin = Admin(app, name=u'后台管理系统')

admin.add_view(processMonitorViews(processMonitor, db.session, name=u'招聘会信息'))