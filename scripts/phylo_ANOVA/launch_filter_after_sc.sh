#!/bin/bash

#SBATCH --array=1-158%100
#SBATCH --nodes=1
#SBATCH -c 1   
#SBATCH -o hello-%j-%a.out


maf=$(ls maf_counts2/ | sed "${SLURM_ARRAY_TASK_ID}q;d")
#value=$(ls maf_by_chrom/maf_8sp/ | sed "${SLURM_ARRAY_TASK_ID}q;d")
maf=${maf::-8}

python scripts_october/check_gene_files.py $maf
