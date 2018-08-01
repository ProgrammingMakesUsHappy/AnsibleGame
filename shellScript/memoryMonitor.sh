#!/bin/bash

URL='http://192.168.3.1:5000/memory/'
while true;
  do
	memInfo=`free -m |awk 'NR==2{print $2,$3,$4,$5,$6,$7}'`
	total=`echo $memInfo|awk '{printf $1}'`
	used=`echo $memInfo|awk '{printf $2}'`
	free=`echo $memInfo|awk '{printf $3}'`
	share=`echo $memInfo|awk '{printf $4}'`
	cache=`echo $memInfo|awk '{printf $5}'`
	available=`echo $memInfo|awk '{printf $6}'`
	HostIP=`/sbin/ifconfig -a|grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d "addr:"|grep -v 172|grep -v 139`
	json='{"total":"'"$total"'","HostIP":"'"$HostIP"'","used":"'"$used"'","free":"'"$free"'","share":'$share',"cache":"'"$cache"'","available":"'"$available"'"}'
        temp=`echo $json`
	echo $memInfo
	echo $json
	result=`curl -H "Accept: application/json"  -H "Content-Type: application/json" -X POST -d "$temp" $URL`
	sleep 180;
  done

