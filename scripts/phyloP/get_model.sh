#!/bin/bash
maf_file=$1
dir=$2

phyloFit --tree '((GCA_008658365,GCA_009819605)BirdsAnc23,((GCA_009819655,GCA_014839755)BirdsAnc44,(GCF_003957565,GCA_009764595)BirdsAnc46)BirdsAnc39);' \
--subst-mod REV $dir/$maf_file --out-root models_by_chrom/all/$maf_file
