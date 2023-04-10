#!/bin/bash

mkdir -p wig_by_chrom

dir=$1
dir2=$2
method=$3

for cond in $(ls $dir2)
do
	for chrom in $(ls $dir)
	do
        	sbatch -c 16 -n 1 -p vgl scripts_october/get_wig_final.sh $dir2/$cond/$chrom.mod $dir/$chrom $chrom $method $cond
	done
done
