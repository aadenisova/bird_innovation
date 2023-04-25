## initial_SNP


### launch_maf_sc.sh

It takes chromosome-specific maf-file (ex. NC_044234.2.maf) and runs maf_screening.py using this maf-file as input.

### maf_screening.py

It finds all positions that fall into groups 1,2 or 3 and writes down the following characteristics for them: start, cons, inno, non_inno, Ref_inno, Alt_noninno, n_inno, n_noninno, n, inno_N, inno_-, noninno_N, noninno_-. Files are saved in a directory maf_counts.

Now you just need to do 

cd coursework_results/maf_counts/
cat * > maf_counts_cated.csv

after launch_maf_sc.sh 
-----------------------------------------------------------------------------------------------------------------------------------------------------------

### launch_get_bed_int.sh

It takes file made with phyloP (ex. NC_044234.2.maf_final) and runs get_bed_int3.py using this maf_final-file as input.

### get_bed_int3.py

It filters out the files received by phyloP those that satisfy the 1st, 2nd or 3rd group. Filters so that there are at least 3 innovative and 3 non-innovative species, and also that in group 1 in both cases there are many rejected substitutions, in group 2 - rejected substitutions only in the innovative group, 3 - only in the non-innovative group.

Files are saved in a directory intervals_by_chrom as two_alleles_CHROM.maf.bed (ex. two_alleles_NC_044216.2.maf.bed)

### launch_get_inno.sh

It takes positions that fall into groups 1,2 or 3 from file in maf_counts (ex. NC_044234.2.maf.csv) and runs get_inno.py using this csv-file as input

### get_inno.py 

It takes files made by get_bed_int3.py from intervals_by_chrom3 (ex. two_alleles_NC_044216.2.maf.bed) and files made by maf_screening.py from maf_counts (ex. NC_044234.2.maf.csv), filters positions from maf_counts: only positions fall into any of 1, 2, 3 can stay and then merge this files together. It saves result to evolved_positions.

### launch_big_table.sh

It runs make_big_table.py.

### make_big_table.py

It goes through all chromosomes and distributes the positions obtained from screening maf-files using the script into groups 1, 2 and 3. In a separate file number_of_nucl.tsv writes the number of positions obtained using conventional screening and screening taking into account phylogenetic information using phyloP. It saves results into two_alleles.tsv, fixed_inno.tsv, fixed_noninno.tsv.
