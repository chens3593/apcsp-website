#!/bin/bash
if [ $# -eq 0 ] ; then
	PI="rpi01 rpi02 rpi03 rpi04 rpi05 rpi06 rpi07 rpi08 rpi09 rpi10 rpi11 rpi12 rpi13 rpi14 rpi15 rpi16 rpi17 rpi18 rpi19 rpi20"
else
	PI=$@
fi

for i in $PI; do
	ping -c 1 -W 10 $i >&-
	if [ $? -eq 0 ] ; then
		echo "$i : alive"
	else
		echo "$i : dead"
	fi
done


exit 0
