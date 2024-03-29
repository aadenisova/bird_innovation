#!/bin/bash

#SBATCH --array=1-199%100
#SBATCH --nodes=1
#SBATCH -c 1   

value=$(ls maf_by_chrom/maf_6sp/ | sed "${SLURM_ARRAY_TASK_ID}q;d")

python bird_innovation/scripts/initial_SNP/maf_screening.py maf_by_chrom/maf_6sp/$value maf_counts6
