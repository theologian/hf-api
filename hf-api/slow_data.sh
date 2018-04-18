#!/bin/bash
sleeptime=$1

if [ "$1" == "" ]; then
echo "sleep 5; echo will be set"
sleeptime=5
fi

while true
 do
  randomp1=`echo $((10 + RANDOM % 100))`
  randomp2=`echo $((10 + RANDOM % 100))`
  curl -X POST http://localhost:3000/?p1=${randomp1}
  curl -X POST http://localhost:3000/?p2=${randomp2}
 sleep $sleeptime
done
