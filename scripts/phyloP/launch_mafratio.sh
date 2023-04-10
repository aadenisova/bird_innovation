#!/bin/bash

dir=$1
program=$2

for file in $(ls $dir)
do
	python3 scripts_october/$program $dir $file	
done
