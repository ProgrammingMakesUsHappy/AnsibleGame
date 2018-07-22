#!/bin/bash

pName=$1 #args input
URL='http://127.0.0.1:5000/testPost/'
ok='ok'
post_json_curl()
{
    curl $1  -H "Accept: application/json"  -H "Content-Type: application/json" -d $2
    #echo $result
    #if [ "$result" = "$ok" ];
    #then
    #     continue;
         #echo $(hostname)
    #else
    #     post_json_curl
         #echo shit!
    #fi

}
while true;
  do
        info=`ps aux |grep "$pName" |grep -v grep | awk 'NR==1{print $3,$4,$9,$10}'`
        RunTime=`echo $info|awk '{print $4}'`
        StartTime=`echo $info|awk '{print $3}'`
        HostIP=`/sbin/ifconfig -a|grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d "
addr:"|grep -v 172`
        CPU=`echo $info|awk '{print $1}'`
        Memory=`echo $info|awk '{print $2}'`
        json='{"HostIP":"'"$HostIP"'","HostName":"'"$(hostname)"'","CPU":"'"$CPU"'","Memory":"'"$Mem
ory"'","RunTime":"'"$RunTime"'","StartTime":"'"$StartTime"'"}'
        result=`post_json_curl $URL $json`;
        if [ "$result" != "$ok" ]; then
                echo failed!;
                sleep 3;
                continue;
        fi
        sleep 30;
  done