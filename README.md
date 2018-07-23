# opsGame
修改代码前先pull
git确认功能修改以后及时提交push

#### opsGame
Flask + Ansible + Pycharm + Python3 + MySQL 
API设计规范：http://www.pythondoc.com/flask-restful/index.html

#### 环境

1. 使用虚拟环境virtualenv
2. pip安装flask及插件、ansible等依赖
3. Flask所需插件flask-sqlalchemy、flask-admin

#### 结构
主机列表hosts放于/etc/ansible/inventory/目录下
inventory文件夹自行创建，hosts自行新建
给一个如下的参考：
```
├── ansible.cfg
├── inventory
│   ├── group_vars
│   │   └── web138
│   ├── hosts
│   ├── host_vars
│   └── readme.md
├── nginx.yaml
├── README.md
└── roles
```  

# API  
### 进程监控
pName（进程名）、HostIP、HostName、CPU、Memory、RunTime、StartTime
```
example:
{'HostIP': '192.168.139.1 192.168.3.1', 'HostName': 'qiushi-X270-W10DG', 'CPU': '0.0', 'Memory': '0.5', 'RunTime': '0:04', 'StartTime': '08:40'}
```
### 文件系统监控
FilePath、HostIP、HostName、FS、Volume、Usage
```
example:
{'FilePath': '/media/qiushi/USB_DISK/test', 'FS': '/dev/sda1', 'Volume': '13G', 'Usage': '22%', 'HostIP': '192.168.139.1 192.168.3.1', 'HostName': 'qiushi-X270-W10DG'}
```

### 心跳进程
HostIP、HostName、HeartTime

# 数据库
### 主机列表
HostIP、HostName、Group （依据赛事举办方提供的列表依情况导入）
### 进程监控表
pName、HostIP、HostName、CPU、Memory、runTime、startTime、Group、Time
(保证一台主机的某一进程信息只有一条最新的数据，即API信息落库时,第一次使用Insert,后面使用update)
### 文件系统监控表
FilePath、HostIP、HostName、FS、Volume、Usage、Time

# SHELL脚本应用
### processmonitor.sh
>进程监控应用，有一个参数 即 进程名或者运行使用的command 如『python runserver.py runserver』
30s更新一次进程信息，如果服务器未准确接收参数，将5s内重新向服务器post 进程的json格式信息
```
example:
    sh monitor.sh 'python runserver.py runserver'
```

### FSMonitor.sh
> 文件系统监控，监控所输入路径所在磁盘分区的使用情况,300s更新一次
```
example：
    sh FSMonitor.sh '/media/qiushi/USB_DISK/test'
 ```