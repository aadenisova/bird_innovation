This repository contains scripts that I use to process files related to the Bird innovation project.

## initial_SNP


### launch_maf_sc.sh: 

It takes chromosome-specific maf-file (ex. NC_044234.2.maf) and runs maf_screening.py using this maf-file as input.

### maf_screening.py

It finds all positions that fall into groups 1,2 or 3 and writes down the following characteristics for them: start, cons, inno, non_inno, Ref_inno, Alt_noninno, n_inno, n_noninno, n, inno_N, inno_-, noninno_N, noninno_-. Files are saved in a directory maf_counts.

### launch_get_bed_int.sh

It takes file made with phyloP (ex. NC_044234.2.maf_final) and runs get_bed_int3.py using this maf_final-file as input.

### get_bed_int3.py

It filters out the files received by phyloP those that satisfy the 1st, 2nd or 3rd group. Filters so that there are at least 3 innovative and 3 non-innovative species, and also that in group 1 in both cases there are many rejected substitutions, in group 2 - rejected substitutions only in the innovative group, 3 - only in the non-innovative group.

Files are saved in a directory intervals_by_chrom as two_alleles_CHROM.maf.bed (ex. two_alleles_NC_044216.2.maf.bed)

### launch_get_inno.sh

It takes positions that fall into groups 1,2 or 3 from file in maf_counts (ex. NC_044234.2.maf.csv) and runs get_inno.py using this csv-file as input.

### get_inno.py 

### launch_big_table.sh

### launch_get_bed_int.sh

### make_big_table.py

### maf_screening.py
           

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
