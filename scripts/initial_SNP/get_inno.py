import numpy as np
import pandas as pd
from sys import argv


chrom = argv[1]

path_evol = 'december/intervals_by_chrom3/'
path_all_chrom = 'maf_counts/'


cons_type = ['two_alleles', 'fixed_inno', 'fixed_noninno']

cons_in_table = ['cons','inno','non_inno']

for i in range(3):

    df_evol = pd.read_csv('{}{}_{}.maf_final.bed'.format(path_evol, cons_type[i], chrom), sep = '\t',
                         names = ['start'])
    df_evol['start'] = df_evol['start']-1
    
    df_all_chrom =  pd.read_csv('{}{}.maf.csv'.format(path_all_chrom, chrom))
    df_checked = df_all_chrom[df_all_chrom[cons_in_table[i]]==True]
    merged_df = df_checked.merge(df_evol, on = 'start', how='inner')
    merged_df['chrom'] = chrom

    merged_df.to_csv('evolved_positions/{}_{}.tsv'.format(cons_type[i], chrom), sep = '\t')