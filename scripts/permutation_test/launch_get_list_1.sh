#!/bin/bash

#SBATCH --nodes=1
#SBATCH -c 1   
#SBATCH -o logi/gene_list-%a.out

for num in {1..35}
do
    python bird_innovation/scripts/permutation_test/get_list_of_genes_1.py $num
done