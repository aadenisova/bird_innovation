#!/bin/bash
maf_file=$1
dir=$2

phyloFit --tree "(GCA_008658365,(GCA_014839755,GCF_003957565)BirdsAnc39);" --subst-mod REV \
$dir/$maf_file --out-root models_by_chrom/noninno/$maf_file
