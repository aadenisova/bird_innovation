#!/bin/bash

dir="bird_innovation/scripts/permutation_test/"

for i in {1..35}
do
    list_inno=$(cat $dir/35_names.txt  | sed "${i}q;d" | awk '{print $1}')
    list_noninno=$(cat $dir/35_names.txt  | sed "${i}q;d" | awk '{print $2}')
    num=$i

    sbatch -p vgl bird_innovation/scripts/permutation_test/launch_maf_sc.sh $list_inno $list_noninno $num
done

#sbatch -p vgl scripts_october/launch_launch_maf_sc.sh 
