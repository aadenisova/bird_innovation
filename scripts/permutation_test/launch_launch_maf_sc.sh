#!/bin/bash

for i in {41..70}
do
    list_inno=$(cat 70_names.txt  | sed "${i}q;d" | awk '{print $1}')
    list_noninno=$(cat 70_names.txt  | sed "${i}q;d" | awk '{print $2}')
    num=$i

    sbatch -p vgl scripts_october/launch_maf_sc.sh $list_inno $list_noninno $num
done

#sbatch -p vgl scripts_october/launch_launch_maf_sc.sh 
