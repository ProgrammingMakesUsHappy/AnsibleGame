#!/bin/bash

pName='ps aux'
URL='http://127.0.0.1:5000/testPost/'
info=`ps aux |grep "$pName" |grep grep | awk 'NR==1{print $3,$4,$9,$10}'`
RunTime=`echo $info|awk '{print $4}'`
StartTime=`echo $info|awk '{print $3}'`
HostIP=`/sbin/ifconfig -a|grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d "addr:"|grep -v 172`
CPU=`echo $info|awk '{print $1}'`
Memory=`echo $info|awk '{print $2}'`
json='{"HostIP":"'"$HostIP"'","HostName":"'"$(hostname)"'","CPU":"'"$CPU"'","Memory":"'"$Memory"'","RunTime":"'"$RunTime"'","StartTime":"'"$StartTime"'"}'
ok='ok'
post_json_curl()
{
    result=`curl $1  -H "Accept: application/json"  -H "Content-Type: application/json" -d $2`
    echo $result
    if [ "$result" = "$ok" ];
    then
            echo $(hostname)
     else
         echo shit!
    fi

}

post_json_curl $URL $json
