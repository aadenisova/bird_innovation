#!/bin/bash

list_of_chrom=$1
align_hal=$2
sp_list=$3
new_dir=$4

mkdir maf_by_chrom
mkdir maf_by_chrom/$new_dir

for chrom in $(less $list_of_chrom)
do
	sbatch -c 16 -n 1 -p vgl scripts_october/to_maf.sh GCF_003957565.2_bTaeGut1.4.pri \
	$chrom $sp_list maf_by_chrom/$new_dir/$chrom.maf $align_hal
done

