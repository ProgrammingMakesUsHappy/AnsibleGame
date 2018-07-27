#!/bin/bash
URL='http://192.168.3.1:5000/pengpeng/'
IP=`/sbin/ifconfig -a|grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d "addr:"|grep -v 172|grep -v 139`
data='{"IP":"'"$IP"'"}'
tdata=`echo $data`
while true;
  do
    curl -H "Accept: application/json"  -H "Content-Type: application/json" -X POST -d $tdata $URL >/dev/null 2>&1
    sleep 3;
  done
