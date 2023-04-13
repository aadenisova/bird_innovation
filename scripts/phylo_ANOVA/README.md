## phylo_ANOVA

## launch_to_maf_big.sh

It runs to_maf_big.sh

## to_maf_big.sh

It runs hal2maf --onlyOrthologs --noDupes 

## launch_filter_after_sc.sh

It runs check_gene_files.py.  Files are saved in a directory maf_by_chrom_big as CHROM.maf  (ex. NC_044234.2.maf)

## check_gene_files.py

It checks that the genes in position_with_genes.tsv also fall into one of three groups when considering multiple alignment (for 38). The result of the check is stored in the chrom_int_anno directory as CHROM.csv (ex. NC_044234.2.csv). The alignment pieces themselves are stored in the chrom_int directory (ex. chrom_int/NC_044215.2_20012544.tsv).

## positions.Rmd

It does a phylogenetic ANOVA
