#!/bin/bash

pName=$1 #args input
URL='http://192.168.3.1:5000/processPost/'
ok='ok'
while true;
  do
        info=`ps aux |grep "$pName" |grep -v grep | awk 'NR==1{print $3,$4,$9,$10}'`
        RunTime=`echo $info|awk '{print $4}'`
        StartTime=`echo $info|awk '{print $3}'`
        HostIP=`/sbin/ifconfig -a|grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d "addr:"|grep -v 172|grep -v 139`
        CPU=`echo $info|awk '{print $1}'`
        Memory=`echo $info|awk '{print $2}'`
        json='{"pName":"'"$pName"'","HostIP":"'"$HostIP"'","HostName":"'"$(hostname)"'","CPU":'$CPU',"Memory":'$Memory',"RunTime":"'"$RunTime"'","StartTime":"'"$StartTime"'"}'
	temp=`echo $json`
	result=`curl -H "Accept: application/json"  -H "Content-Type: application/json" -X POST -d "$temp" $URL`
	echo $result
	if [ "$result" != "$ok" ]; then
                echo failed!;
                sleep 3;
                continue;
        fi
        sleep 30;
  done
