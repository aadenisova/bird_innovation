#!/bin/bash

#SBATCH --nodes=1
#SBATCH -c 1   
#SBATCH -o logi/log-%j-%a.out

for i in {1..35}
do
cat coursework_results/permutation_test/$i/* > coursework_results/permutation_test_cated/$i.csv
done
