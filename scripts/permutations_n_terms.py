import gffpandas.gffpandas as gffpd

import pandas as pd
from pandas.core.common import SettingWithCopyWarning
import gseapy as gp
import warnings

import numpy as np
from gseapy.plot import barplot, dotplot
from matplotlib import pyplot as plt 


warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
path_to_data=''


annotation = gffpd.read_gff3('{}{}'.format(path_to_data, 'GCF_003957565.2_bTaeGut1.4.pri_genomic.gff'))

df_ori = annotation.df
df_ori['chrom']=df_ori['seq_id']
df = df_ori[df_ori['type']=='gene']

df['element_ID'] = df['attributes'].apply(lambda x: x.split(';')[0].split('=')[1].split('-')[1])
background = df['element_ID'].tolist()


go_BP = gp.get_library(name='GO_Biological_Process_2021', organism='Human')
go_MF = gp.get_library(name='GO_Molecular_Function_2021', organism='Human')
go_CC = gp.get_library(name='GO_Cellular_Component_2021', organism='Human')
go_reactome = gp.get_library(name='Reactome_2016', organism='Human')


def get_df(database, genelist, background):
    enr = gp.enrichr(gene_list=genelist ,
        gene_sets=database,
        background = background,  
        outdir=None,
        cutoff=0.5,                          
     )
    return enr


def check_bigger(p_x, p_y):
    if p_y or p_x<p_y:
        return 0
    else:
        return 1

names = ['go_BP', 'go_MF', 'go_CC', 'go_reactome']
proc = [go_BP, go_MF, go_CC, go_reactome]

for go in range(len(proc)):

    i=1
    file = open('dir_gene_list/gene_list_{}.txt'.format(i)).read()
    genelist = file.split('\n')

    df_proc = get_df(proc[go], genelist, background).res2d
    df_proc = df_proc[df_proc['Adjusted P-value']<0.05]
    df_to_check = df_proc[['Term', 'Adjusted P-value']].reset_index(drop=True)

    df_to_merge = df_proc.loc[:, ~df_proc.columns.isin(['Term', 'Adjusted P-value'])].reset_index(drop=True)

    #df_to_check['is_smaller'] = 1
    #df_to_check['n'] = 1

    for i in range(2, 71):
        file = open('dir_gene_list/gene_list_{}.txt'.format(i)).read()
        genelist = file.split('\n')

        df_proc = get_df(proc[go], genelist, background).res2d
        #df_proc = df_proc[df_proc['Adjusted P-value']<0.05]

        new_df = df_to_check.merge(df_proc, on = 'Term', how='left')
        new_df = new_df.rename(columns = {'Adjusted P-value_y': str(i), 'Adjusted P-value_x': 'Adjusted P-value'})
        df_to_check = new_df.drop(columns = ['Gene_set', 'Overlap', 'P-value','Odds Ratio', 'Genes'])
        #new_df['is_smaller'] = new_df.apply(lambda x: check_bigger(x['Adjusted P-value_x'], x['Adjusted P-value_y']), axis=1)
        #df_to_check['is_smaller']+=new_df['is_smaller']
        #df_to_check['n']+=1

        
    df_to_merge.join(df_to_check).to_csv('permutations_n_terms_{}_new2.csv'.format(names[go]), index = False)
