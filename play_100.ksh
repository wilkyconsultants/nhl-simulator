#!/bin/ksh
c=1
while [[ $c -le 100 ]]; do
	./NHL.py
	(( c++ ))
done
