This repository contains scripts that I use to process files related to the Bird innovation project.

## initial_SNP


### launch_maf_sc.sh: 

It takes chromosome-specific maf-file (ex. NC_044234.2.maf) and runs maf_screening.py using this maf-file as input.

###maf_screening.py

It finds all positions that fall into groups 1,2 or 3 and writes down the following characteristics for them: start, cons, inno, non_inno, Ref_inno, Alt_noninno, n_inno, n_noninno, n, inno_N, inno_-, noninno_N, noninno_-. Files are saved in a directory maf_counts.

get_bed_int3.py  launch_big_table.sh    launch_get_inno.sh  maf_screening.py
get_inno.py      launch_get_bed_int.sh      make_big_table.py


## SNP_analysis


Gene_SNP_analysis.ipynb

Plot_pos_dict.ipynb

bash_snpEff.sh

tRNA_search.ipynb

## permutation_test


combinations_for_permutations.py

launch_launch_maf_sc.sh

launch_maf_sc.sh

launch_n_terms.sh

maf_screening.py

make_big_file.sh

permutation_analysis.ipynb

permutational.py

permutations_n_terms.py


## phylo_ANOVA


positions.Rmd
