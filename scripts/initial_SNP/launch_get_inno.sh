#!/bin/bash

#SBATCH -o hello-%j.out
#SBATCH --array=1-199%100
#SBATCH --nodes=1
#SBATCH -c 1   

ans=$(ls coursework_results/maf_counts/ | sed "${SLURM_ARRAY_TASK_ID}q;d")
chrom=${ans::-8}

python bird_innovation/scripts/initial_SNP/get_inno.py $chrom
