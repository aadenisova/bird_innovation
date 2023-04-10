#!/bin/bash

#SBATCH --array=1-199%100
#SBATCH --nodes=1
#SBATCH -c 1   

value=$(ls maf_by_chrom/maf_8sp/ | sed "${SLURM_ARRAY_TASK_ID}q;d")

python scripts_october/maf_screening.py maf_by_chrom/maf_8sp/$value
