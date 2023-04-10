#!/bin/bash

dir=$1
dir2=$2
method=$3
output_format=$4
dir_to_make=$5

mkdir -p $dir_to_make

for cond in $(ls $dir)
do
        mkdir -p $dir_to_make/$cond

        for chrom in $(ls $dir/$cond)
        do
                sbatch -c 16 -n 1 -p vgl scripts_october/get_wig_final.sh $dir2/$cond/$chrom.mod $dir/$cond/$chrom $chrom \
		$method $cond $output_format $dir_to_make
        done
done


