#!/bin/bash

#SBATCH --nodes=1
#SBATCH -c 1   
#SBATCH -o logi/hello_2-%j-%a.out

value=$1
i=$2

dir="bird_innovation/scripts/permutation_test/"

list_inno=$(cat $dir/35_names.txt  | sed "${i}q;d" | awk '{print $1}')
list_noninno=$(cat $dir/35_names.txt  | sed "${i}q;d" | awk '{print $2}')

num=$i

echo $value $num
python bird_innovation/scripts/permutation_test/maf_screening.py maf_by_chrom_big/$value $list_inno $list_noninno $num
