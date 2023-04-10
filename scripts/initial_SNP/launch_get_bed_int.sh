#!/bin/bash

#SBATCH -o hello-%j.out
#SBATCH --array=1-199%100
#SBATCH --nodes=1
#SBATCH -c 1   

chrom=$(ls december/b_by_b_final/maf_8sp/ | sed "${SLURM_ARRAY_TASK_ID}q;d")

python scripts_october/get_bed_int3.py $chrom december/b_by_b_final/ december/intervals_by_chrom3 


