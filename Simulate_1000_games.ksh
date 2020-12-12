#!/bin/ksh
ctr=0
while (( ctr < 10 ))
do
	nohup ./play_100.ksh >/dev/null &
	(( ctr = ctr + 1 ))
done
