#!/bin/bash

new_dir=$1
dir=$2

mkdir $new_dir
cd $new_dir
mkdir all inno noninno
cd ../

for chrom in $(ls $dir)
do
	sbatch -c 16 -n 1 -p vgl scripts_october/get_model.sh $chrom $dir
	sbatch -c 16 -n 1 -p vgl scripts_october/get_model_inno.sh $chrom $dir
	sbatch -c 16 -n 1 -p vgl scripts_october/get_model_noninno.sh $chrom $dir
done

