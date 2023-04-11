#!/bin/bash

#SBATCH -J hello
#SBATCH --array=1-200%100                   # how many tasks in the array 24749
#SBATCH -c 1                            # one CPU core per task
#SBATCH --nodes=1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=savouriess2112@gmail.com

list_of_chrom=$1
align_hal=$2

chrom=$(less $list_of_chrom | sed "${SLURM_ARRAY_TASK_ID}q;d")
. scripts_october/to_maf_big.sh GCF_003957565.2_bTaeGut1.4.pri \
$chrom maf_by_chrom_big/$chrom.maf $align_hal
