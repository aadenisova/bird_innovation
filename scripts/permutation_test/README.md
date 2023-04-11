## Permutation test

### combinations_for_permutations.py

Records all ways to make 2 groups of 8 bird species

### launch_launch_maf_sc.sh

It takes two combinations of 4 types each and runs launch_maf_sc.sh using these lists as input.

### launch_maf_sc.sh

It takes two combinations of 4 types each and runs maf_screening.py using these lists and maf-files for each chromosome as input.

### maf_screening.py

It finds all positions that fall into groups 1,2 or 3 and writes down the following characteristics for them: start, cons, inno, non_inno, Ref_inno, Alt_noninno, n_inno, n_noninno, n, inno_N, inno_-, noninno_N, noninno_-. Files are saved in a directory permutation_test/number_of_combination/chrom (ex. permutation_test/1/NC_044234.2.maf.csv).

### make_big_file.sh

It cats all files in permutation_test/number_of_combination (ex. permutation_test/1/) into one file (ex. permutation_test/1.csv)

### launch_permutations.sh (absent)

It runs permutational.py for each permutation

### permutational.py

It calsulates set of genes for each permutation

### launch_n_terms.sh

It runs permutations_n_terms.py

### permutations_n_terms.py

For each previously calculated set of genes, it performs an analysis of enrichment in 4 bases (BP, CC, MF, Reactome). Files are saved in permutations_n_terms_TYPE_OF_DATASET_new2.csv (ex. permutations_n_terms_go_CC_new2.csv)

### permutation_analysis.ipynb

It plots and analyzes which terms have been filtered
