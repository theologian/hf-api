#!/bin/bash
sleeptime=$1

if [ "$1" == "" ]; then
echo "sleep 5; echo will be set"
sleeptime=5
fi

while true
 do
  randomp1=`echo $((4 + RANDOM % 160899))`
  randomp2=`echo $((8 + RANDOM % 159342))`
  curl -X POST http://localhost:3000/?p1=${randomp1}
  curl -X POST http://localhost:3000/?p2=${randomp2}
 sleep $sleeptime
done
