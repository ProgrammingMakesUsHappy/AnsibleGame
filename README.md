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
pName（进程名）、HostIP、HostName、CPU、Memory、runTime、startTime

# 数据库
### 主机列表
HostIP、HostName、Group （依据赛事举办方提供的列表依情况导入）
### 进程监控表
pName、HostIP、HostName、CPU、Memory、runTime、startTime、Group
### 资源监控表
