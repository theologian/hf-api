#!/bin/bash

while true
 do
  randomp1=`echo $((10 + RANDOM % 100))`
  randomp2=`echo $((10 + RANDOM % 100))`
  curl -X POST http://localhost:3000/?p1=${randomp1}
  curl -X POST http://localhost:3000/?p2=${randomp2}
 sleep 5
done
