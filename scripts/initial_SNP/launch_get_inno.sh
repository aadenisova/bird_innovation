#!/bin/bash

#SBATCH -o hello-%j.out
#SBATCH --array=1-199%100
#SBATCH --nodes=1
#SBATCH -c 1   

ans=$(ls maf_counts/ | sed "${SLURM_ARRAY_TASK_ID}q;d")
chrom=${ans::-8}

python scripts_october/get_inno.py $chrom