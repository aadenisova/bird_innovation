import pandas as pd
import numpy as np


cons_type = ['two_alleles', 'fixed_inno', 'fixed_noninno']
cons_in_table = ['cons','inno','non_inno']

chr_names = pd.read_csv("chr_names.tsv", sep='\t')
chr_names.head()


df_allt_all = []
df_alli_all = []
df_alln_all = []

li = ['chrom\ttwo_evolved\ttwo_all\tinno_evolved\tinno_all\tnoninno_evolved\tnoninno_all']
for i in chr_names['chrom'][:36]:
    df_all_ = pd.read_csv('maf_counts/{}.maf.csv'.format(i))
    df_all_['chrom'] = i

    df_allt = df_all_[(df_all_[cons_in_table[0]]==True) & (df_all_['n']>=6)]
    df_allt_all.append(df_allt)

    df_alli = df_all_[(df_all_[cons_in_table[1]]==True) & (df_all_['n']>=6)]
    df_alli_all.append(df_alli)

    df_alln = df_all_[(df_all_[cons_in_table[2]]==True) & (df_all_['n']>=6)]
    df_alln_all.append(df_alln)

    df = pd.read_csv('evolved_positions/{}_{}.tsv'.format(cons_type[0], i), sep = '\t')
    dft = df[df['n'] >= 6]

    df = pd.read_csv('evolved_positions/{}_{}.tsv'.format(cons_type[1], i), sep = '\t')
    dfi = df[df['n'] >= 6]

    df = pd.read_csv('evolved_positions/{}_{}.tsv'.format(cons_type[2], i), sep = '\t')
    dfn = df[df['n'] >= 6]

    
    li.append('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(i, dft.shape[0], df_allt.shape[0], dfi.shape[0], df_alli.shape[0], dfn.shape[0], df_alln.shape[0]))

f = open('number_of_nucl.tsv', 'w')
f.write('\n'.join(li))
f.close()

pd.concat(df_allt_all).to_csv('{}.tsv'.format(cons_type[0]), sep = '\t')
pd.concat(df_alli_all).to_csv('{}.tsv'.format(cons_type[1]), sep = '\t')
pd.concat(df_alln_all).to_csv('{}.tsv'.format(cons_type[2]), sep = '\t')


