from sys import argv
import numpy as np
import pandas as pd

chrom = argv[1] #'NW_024545460.1.maf'
#path = argv[2] #'wig_by_chrom/'
path_final = argv[2] #'wig_by_chrom_final/'
path_interval = argv[3] #'intervals_by_chrom', куда в итоге будешь сохранять файлы

"""
Чтение файла .wig с посчитанными scor'ами 
для каждого нуклеотида
"""

def rates_open(path_final, type_wig=None):
    names = ['#nneut', 'nobs', 'nrej', 'nspec']
    
    rates1 = pd.read_csv(path_final, 
                    sep = '\t',
                    names = names,
                    )
    rates1 = rates1[['nrej', 'nspec']]
    rates1 = rates1[rates1['nspec']>=3] #3 - кол-во видов в выравнивании инновационных видов
    return rates1

"""
Получение из .wig файлов интервалов, 
которые в дальнейшем будут извлечены из .maf файла
"""

#def get_intervals(rates_filter, name, chrom):

    # start = []
    # end = []

    # prev = 0
    # counter = 0
    # for i in rates_filter['index']:
    #     if prev==0:
    #         prev = i
    #     else:
    #         if (i-prev) == 1:
    #             counter+=1
    #             prev = i
    #         else:
    #             start.append(prev-counter)
    #             end.append(prev)
    #             counter = 0
    #             prev = i
                
    # start.append(prev-counter)
    # end.append(prev)

    # df = pd.DataFrame({'chrom':chrom,'start':start, 'end':end})
    # df['index'] = df['start'].astype(str)+'-'+df['end'].astype(str)
    # df.to_csv(name, sep = '\t', index = False, header = False)       

def get_table(chrom, path_final, typ):
    #ratesI_s = get_coord(path+'/'+typ+'/'+chrom)[1:]
    ratesI = rates_open(path_final+'/'+typ+'/'+chrom)
    #ratesI.index = ratesI_s
    #ratesI.index  = ratesI.index -1
    ratesI=ratesI.rename(columns={'nrej':'lnlratio_'+typ})
    return ratesI

def save(rates_filter, name):

    rates_filter['start'] =  rates_filter['index']
    rates_filter['start'].to_csv(name, sep = '\t', index = False, header = False) 



ratesI = get_table(chrom,  path_final, 'maf_4sp_inno')
ratesNI = get_table(chrom, path_final, 'maf_4sp_noninno')
ratesAll = get_table(chrom, path_final, 'maf_8sp')

rates = pd.concat([ratesI, ratesNI, ratesAll], axis=1)
rates['index'] = rates.index
rates=rates.dropna()

pd.options.mode.chained_assignment = None 
rates_filter = rates[rates!=0].dropna()
rates_filter1 = rates_filter[(rates_filter['lnlratio_maf_4sp_inno']>0)]

save(rates_filter1, '{}/fixed_inno_{}.bed'.format(path_interval, chrom))

#ищем участки с зафиксировавшейся мутацией в неиновационных и разным аллелем у инновационных

rates_filter = rates[rates!=0].dropna()
rates_filter2 = rates_filter[(rates_filter['lnlratio_maf_4sp_noninno']>0)]

save(rates_filter2, '{}/fixed_noninno_{}.bed'.format(path_interval, chrom))

#ищем участки с зафиксировавшейся мутацией в обоих группах, но разными аллелями

rates_filter3 = rates_filter[(rates_filter['lnlratio_maf_4sp_noninno']>0)&
                            (rates_filter['lnlratio_maf_4sp_inno']>0)&
                            (rates_filter['lnlratio_maf_8sp']<0)]


save(rates_filter3, '{}/two_alleles_{}.bed'.format(path_interval, chrom))