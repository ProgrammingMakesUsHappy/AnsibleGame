#!/bin/bash
path=$1
URL='http://127.0.0.1:5000/filesystem/'
info=`df -h $path |awk 'NR==2{print $1,$2,$3,$4,$5}'`
fs=`echo $info |awk '{print $1}'`
volume=`echo $info |awk '{print $2}'`
Usage=`echo $info |awk '{print $5}'`
HostIP=`/sbin/ifconfig -a|grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d "addr:"|grep -v 172`
data='{"FilePath":"'"$path"'","FS":"'"$fs"'","Volume":"'"$volume"'","Usage":"'"$Usage"'","HostIP":"'"$HostIP"'","HostName":"'"$(hostname)"'"}'
Tdata=`echo $data`
ok='ok'
while true;
  do
     result=`curl -H "Accept: application/json"  -H "Content-Type: application/json" -X POST -d "$Tdata" $URL`
     if [ "$result" != "$ok" ]; then
        echo failed!;
        sleep 3;
        continue;
     fi
     sleep 300;
  done

