#!/bin/bash

#SBATCH --array=1-199%5
#SBATCH --nodes=1
#SBATCH -c 1   
#SBATCH -o hello-%j-%a.out

list_inno=$1
list_noninno=$2
num=$3

value=$(ls maf_by_chrom_big/ | sed "${SLURM_ARRAY_TASK_ID}q;d")
#value=$(ls maf_by_chrom/maf_8sp/ | sed "${SLURM_ARRAY_TASK_ID}q;d")

python scripts_october/maf_screening.py maf_by_chrom_big/$value $list_inno $list_noninno $num


#sbatch -p vgl scripts_october/launch_maf_sc.sh 2_bTaeGut1,1_bAlcTor1,1_bSylBor1,1_bBucAby1 1_bGeoTri1,1_bSteHir1,1_bSylAtr1,4_bAquChr1 1
