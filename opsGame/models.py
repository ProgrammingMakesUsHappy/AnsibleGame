# -*- endcoding=UTF-8 -*-

from opsGame import db


class processMonitor(db.Model):
    __tablename__ = 'processMonitor'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    pNameAndIP = db.Column(db.String(45), primary_key=True)
    pName = db.Column(db.String(45), nullable=False)
    HostIP = db.Column(db.String(45), nullable=False)
    HostName = db.Column(db.String(45), nullable=False)
    CPU = db.Column(db.Float, nullable=False)
    Memory = db.Column(db.Float, nullable=False)
    RunTime = db.Column(db.String(45), nullable=False)
    StartTime = db.Column(db.String(45), nullable=False)
    Group = db.Column(db.String(45))
    Time = db.Column(db.String(45), nullable=False)


    def __init__(self, *args):
        if not args :
            self.pNameAndIP = "192.168.1.1:"+"top"
            self.pName = 'TestScholl'
            self.HostName = "TestLocation"
            self.HostIP = "192.168.1.1"
            self.CPU = 0.0
            self.Memory = 0.0
            self.RunTime = "00:00"
            self.StartTime = "00:00"
            self.Group = "null"
            self.Time = "2018-07-25 11:59"
        elif args:
            self.pName = args[0]
            self.HostName = args[1]
            self.HostIP = args[2]
            self.CPU = args[3]
            self.Memory = args[4]
            self.RunTime = args[5]
            self.StartTime = args[6]
            self.Group = args[7]
            self.Time = args[8]
            self.pNameAndIP = args[9]


    def __iter__(self):
        return [self.pName,
                self.HostIP,
                self.HostName,
                self.CPU,
                self.Memory,
                self.RunTime,
                self.StartTime,
                self.Group,
                self.Time,
                self.pNameAndIP]


class fileSystemMonitor(db.Model):
    __tablename__ = 'fileSystemMonitor'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    HostIP = db.Column(db.String(45), nullable=False)
    HostName = db.Column(db.String(45), nullable=False)
    FilePath = db.Column(db.String(128), primary_key=True, nullable=False)
    FS = db.Column(db.String(128), nullable=False)
    Volume = db.Column(db.String(45), nullable=False)
    Usage = db.Column(db.Integer, nullable=False)
    Time = db.Column(db.String(45), nullable=False)
    Group = db.Column(db.String(45))


    def __init__(self, *args):
        if not args :
            self.FilePath = 'TestScholl'
            self.HostName = "TestLocation"
            self.HostIP = "192.168.1.1"
            self.FS = "/dev/sda1"
            self.Volume = "0"
            self.Usage = 0
            self.Time = "2018-07-25 11:59"
            self.Group = "web"

        elif args:
            self.FilePath = args[0]
            self.HostIP = args[1]
            self.HostName = args[2]
            self.FS = args[3]
            self.Volume = args[4]
            self.Usage = args[5]
            self.Time = args[6]
            self.Group = args[7]



    def __iter__(self):
        return [self.FilePath,
                self.HostIP,
                self.HostName,
                self.FS,
                self.Volume,
                self.Usage,
                self.Time,
                self.Group]


class hosts(db.Model):
    __tablename__ = 'hosts'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    hostIP = db.Column(db.String(45), primary_key=True, nullable=False)
    hostName = db.Column(db.String(45), nullable=True)
    hostGroup = db.Column(db.String(45), nullable=False)
    status = db.Column(db.Integer, nullable= False ,default=0)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, *args):
        if not args :
            self.hostIP = ''
            self.hostName = "deafult"
            self.hostGroup = ''
            self.status = 0
            self.timestamp = '1970-01-01 23:59:59'

        elif args:
            self.hostIP = args[0]
            self.hostName = args[1]
            self.hostGroup = args[2]
            self.status = args[3]
            self.timestamp = args[4]

    def __iter__(self):
        return [self.hostIP,
                self.hostName,
                self.hostGroup,
                self.status,
                self.timestamp]


class memoryMonitor(db.Model):
    __tablename__ = 'memorymonitor'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    hostIP = db.Column(db.String(45),  primary_key=True, nullable=False)
    total = db.Column(db.Integer)
    used = db.Column(db.Integer)
    free = db.Column(db.Integer)
    share = db.Column(db.Integer)
    cache = db.Column(db.Integer)
    available = db.Column(db.Integer)
    time = db.Column(db.DateTime, nullable=False)

    def __int__(self, *args):
        if not args:
            self.hostIP = '1.1.1.1'
            self.time = '2018-08-01 00:00:00'
            self.available = 0
            self.cache = 0
            self.free = 0
            self.share = 0
            self.total = 0
            self.used = 0
        else:
            self.total = args[0]
            self.used  = args[1]
            self.free  = args[2]
            self.share = args[3]
            self.cache = args[4]
            self.available= args[5]
            self.time = args[6]
            self.hostIP = args[7]

    def __iter__(self):
        return[self.hostIP,
               self.time,
               self.available,
               self.used,
               self.total,
               self.share,
               self.free,
               self.cache]

