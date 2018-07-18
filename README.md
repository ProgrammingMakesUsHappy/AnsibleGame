# opsGame

#### opsGame
Flask + Ansible + Pycharm + Python3 
后期增加mysql等

#### 环境

1. 使用虚拟环境virtualenv
2. pip安装flask及插件、ansible等依赖

#### 结构
主机列表hosts放于/etc/ansible/inventory/目录下
inventory文件夹自行创建，hosts自行新建
给一个如下的参考：
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
