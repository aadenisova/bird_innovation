#!/bin/bash
mkdir -p intervals_from_maf
for chrom in $(ls intervals_by_chrom)
do 
	. scripts_october/get_int.sh intervals_by_chrom/$chrom intervals_from_maf/${chrom::-8} ${chrom::-8}  

done

for chrom2 in $(ls intervals_from_maf)
do
	echo $chrom2
	. scripts_october/launch_mafratio.sh intervals_from_maf/$chrom2/  maf_ratio_strict.py 
done

