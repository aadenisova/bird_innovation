from sys import argv
import pandas as pd
import numpy as np
import warnings
import gffpandas.gffpandas as gffpd
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

num = argv[1] #'1'

path_to_data='/vggpfs/fs3/vgl/store/adenisova/data/innovation/branch_analysis/test_october/test_gerp/coursework_results/'

order = pd.read_csv(f'{path_to_data}initial_data/sorted_inno_sp.csv')
order = order.rename(columns = {'VGL ID':'sp2'})

cons_in_table = ['cons','inno','non_inno']

all_dfs = []
for i in range(3):
    df = pd.read_csv(f'{path_to_data}permutation_test_cated/{num}.csv',
                     names=['start', 'cons', 'inno', 'non_inno', 'Ref_inno', 
                              'Alt_noninno','n_inno', 'n_noninno', 'n', 'inno_N', 
                              'inno_-', 'noninno_N', 'noninno_-', 'chrom'])
    df['start'] = df['start']+1
    df['type'] = cons_in_table[i]
    
    df3 = df[(((df['n_inno']==4)&(df['n_noninno']==4)) |
              ((df['n_inno']==3)&(df['n_noninno']==4)) | #&((df['inno_N']<=1)|(df['inno_-']<=1)))|
              ((df['n_noninno']==3)&(df['n_inno']==4))  #&((df['noninno_N']<=1)|(df['noninno_-']<=1)))
             )
             &(df[cons_in_table[i]]==True)
              ]

    print(f'number of positions:  {df3.shape[0]}')
    all_dfs.append(df3)
    
df = pd.concat(all_dfs)
df_chrom = pd.read_csv(f'{path_to_data}initial_data/chroms_zebra.tsv', sep = '\t')[:-1]
df_chrom['Molecule name'] = df_chrom['Molecule name'].apply(lambda x: x.split()[1])
df1 = df_chrom[['RefSeq sequence', 'Molecule name']].rename(columns= {'RefSeq sequence':'chrom'})
df1.head()

df_p = df
    
df2 = pd.merge(df1,df_p, on='chrom').rename(columns = {
                                                    'chrom':'#CHROM', 'start':'POS', 
                                                    'Alt_noninno':'ALT', 'Ref_inno':'REF'}) #меняю ALT и REF потому что внутри этих 35 сначала подаются инновационные и там zebra finch; это исправление важно только для snpEff
df2['ID'] = '.'
df2['FILTER'] = '.'
df2['INFO'] = '.'
df2['POS'] = df2['POS']

df3 = df2[['#CHROM', 'POS','ID',  'REF','ALT', 'FILTER', 'INFO', 'type']]

df3.to_csv(f'{path_to_data}permutation_test_vcf/positions_for_8_{num}.vcf', 
            index = False,
            sep = '\t')