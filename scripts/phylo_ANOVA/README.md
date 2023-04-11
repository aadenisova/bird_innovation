## phylo_ANOVA

## launch_to_maf_big.sh

It runs to_maf_big.sh

## to_maf_big.sh

It runs hal2maf --onlyOrthologs --noDupes 

## launch_filter_after_sc.sh

It runs check_gene_files.py

## check_gene_files.py

It checks that the genes taken from position_with_genes.tsv in the multiple alignment also satisfy the condition. For this, multiple alignments for 38 from maf_by_chrom_big are used. Files are saved in a directory chrom_int_anno as CHROM.csv (ex. NC_044234.2.csv)

## positions.Rmd

It does a phylogenetic ANOVA
