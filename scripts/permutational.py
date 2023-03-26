import gffpandas.gffpandas as gffpd

import pandas as pd
from pandas.core.common import SettingWithCopyWarning
import gseapy as gp
import warnings

import numpy as np
from gseapy.plot import barplot, dotplot
from matplotlib import pyplot as plt 

from sys import argv

warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
path_to_data=''


annotation = gffpd.read_gff3('{}{}'.format(path_to_data, 'GCF_003957565.2_bTaeGut1.4.pri_genomic.gff'))

df_ori = annotation.df
df_ori['chrom']=df_ori['seq_id']
df = df_ori[df_ori['type']=='gene']

df['element_ID'] = df['attributes'].apply(lambda x: x.split(';')[0].split('=')[1].split('-')[1])
background = df['element_ID'].tolist()



i = str(argv[1])

df2 = pd.read_csv('{}{}'.format(path_to_data, 'permutation_test/'+i+'.csv'))
df2 = df2[df2['start']!='start'].to_csv('{}{}'.format(path_to_data, 'permutation_test/'+i+'.csv'), index = False)

df2 = pd.read_csv('{}{}'.format(path_to_data, 'permutation_test/'+i+'.csv'))

df2['start'] = df2['start']+1 
df3 = df2[(((df2['n_inno']>=4)&(df2['n_noninno']>=4)) |
              (((df2['n_inno']==3)&(df2['n_noninno']==4))&((df2['inno_N']==1)|(df2['inno_-']==1)))|
             (((df2['n_noninno']==3)&(df2['n_inno']==4))&((df2['noninno_N']==1)|(df2['noninno_-']==1))))]

matched_list = []

for chrom in df3['chrom'].unique():
    df3_chrom = df3[df3['chrom']== chrom]
    df_chrom = df[df['chrom']==chrom]

    for idx in df3_chrom.index:
        df_small = df_chrom[(df_chrom['start']<=df3_chrom.loc[idx]['start'])
                                    &(df_chrom['end']>=df3_chrom.loc[idx]['start'])]
        df_small['coord'] = int(df3_chrom.loc[idx]['start'])
        df_small['coord'] = int(df3_chrom.loc[idx]['start'])
        df_small['coord'] = df_small['coord'] - 1
        matched_list.append(df_small)

df_genes = pd.concat(matched_list)

df_genes['element_ID'] = df_genes['attributes'].apply(lambda x: x.split(';')[0].split('=')[1].split('-')[1])

genelist = list(set(df_genes['element_ID'].to_list()))

file = open('dir_gene_list2/gene_list_{}.txt'.format(i), 'w')
file.write('\n'.join(genelist))
file.close()
