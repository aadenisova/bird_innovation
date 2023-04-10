#!/bin/bash
mkdir wig_by_chrom
cd wig_by_chrom
mkdir all inno noninno noninno3
cd ../

dir=$1
dir2=$2
method=$3

for chrom in $(ls $dir)
do
	sbatch -c 16 -n 1 -p vgl scripts_october/get_wig.sh $dir2/all/$chrom.mod $dir/$chrom $chrom $method
	sbatch -c 16 -n 1 -p vgl scripts_october/get_wig_inno.sh $dir2/inno/$chrom.mod $dir/$chrom $chrom $method
	sbatch -c 16 -n 1 -p vgl scripts_october/get_wig_noninno.sh $dir2/noninno/$chrom.mod $dir/$chrom $chrom $method
	sbatch -c 16 -n 1 -p vgl scripts_october/get_wig_noninno3.sh $dir2/noninno3/$chrom.mod $dir/$chrom $chrom $method
done

