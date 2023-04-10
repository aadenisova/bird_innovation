#!/bin/bash
maf_file=$1
dir=$2

phyloFit --tree "(GCA_009819605,(GCA_009819655,GCA_009764595)BirdsAnc39);" \
--subst-mod REV $dir/$maf_file --out-root models_by_chrom/inno/$maf_file


