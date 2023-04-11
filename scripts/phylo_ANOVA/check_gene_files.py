import pandas as pd
import numpy as np
from Bio import AlignIO
from sys import argv

list_inno = ['2_bCatUst1',
 '1_bGeoTri1',
 '1_bSylAtr1',
 '1_bSteHir1',
 '2_bEriRub2',
 '1_bCorMon1',
 '4_bAquChr1',
 '1_bHirRus1']
#["1_bSylBor1", "2_bTaeGut1", "1_bBucAby1", "1_bAlcTor1" '1_bCapEur3']
list_noninno = ['1_bAlcTor1', '1_bCarCri1',
 '1_bCicMag1',
 '1_bPorHoc1',
 '1_bBucAby1',
 '1_bChiLan1',
 '2_bTaeGut1',
 '1_bNycGra1',
 '1_bPteGut1',
 '1_bCucCan1',
 '1_bAytFul2',
 '1_bPhoRub2',
 '1_bPogPus1',
 '2_bFalNau1',
 '1_bPluApr1',
 '1_bSylBor1',
 '1_bHemCom1',
 '2_bStrTur1',
 '1_bCalAnn1_v1',
 '1_bTheCae1',
 '1_bMerNub1',
 '1_bBalReg1',
 '1_bApuApu2',
 '1_bGalGal1',
 '2_bGalGal1',
 '1_bFalRus1',
 '1_bAcaChl1',
 '2_bCygOlo1',
 '1_bTroSur1']


def is_in_list(name, list_of):
    ans = False
    for bird in list_of:
        if bird in name:
            ans = True
    return ans  

def check(matrix, num):

    if matrix.shape[1]>0:
    
        return np.array([(matrix[:,num] == 'A').sum(),
                        (matrix[:,num] == 'T').sum(),
                        (matrix[:,num] == 'G').sum(),
                        (matrix[:,num] == 'C').sum(),
                        ]), np.array([(matrix[:,num] == 'N').sum(),
                        (matrix[:,num] == '-').sum()])
    else:
        return np.array([0,0,0,0]), np.array([0,0])
    
    
def get_annotation(inno_array, noninno_array, idx, inno_exept, noninno_exept):
    
    list_of = np.array(['A', 'T', 'G', 'C'])  
    
    max_inno = inno_array.sum()
    max_noninno = noninno_array.sum()
    
    cons = (bool((inno_array==max_inno).sum() and (noninno_array==max_noninno).sum()) 
        & (inno_array.argmax() != noninno_array.argmax()))

    inno = (cons==False) and (bool((inno_array==max_inno).sum()) and noninno_array[inno_array.argmax()]==0)

    non_inno = (cons==False) and (bool((noninno_array==max_noninno).sum()) and inno_array[noninno_array.argmax()]==0)
    
    return [idx, cons, inno, non_inno, ','.join(list(list_of[inno_array!=0])),
                            ','.join(list(list_of[noninno_array!=0])), 
                            max_inno,
                            max_noninno,
                            max_inno+max_noninno,
                            inno_exept[0],
                            inno_exept[1],
                            noninno_exept[0],
                            noninno_exept[1]]


def get_df_with_counts(align, idxs_coords, chrom_int):
    for idx in idxs_coords:
        
        
        
        align_dict = {'inno':[[],[]], 'non_inno': [[], []]}
        for seqreq in align:

                sequence = [*(seqreq[0].upper())]

                if is_in_list(seqreq[1], list_inno):

                    align_dict['inno'][1].append(sequence)
                    align_dict['inno'][0].append(seqreq[1])

                elif is_in_list(seqreq[1], list_noninno):

                    align_dict['non_inno'][1].append(sequence)
                    align_dict['non_inno'][0].append(seqreq[1])

                    if "2_bTaeGut1" in seqreq[1]:
                        start = seqreq[2]
                        length = seqreq[3]

        finded_idx = idx -start
                        
        align_dict['inno'][1] = np.matrix(align_dict['inno'][1])
        align_dict['non_inno'][1] = np.matrix(align_dict['non_inno'][1])
        
        inno_array, inno_exept = check(align_dict['inno'][1], finded_idx)
        noninno_array, noninno_exept = check(align_dict['non_inno'][1], finded_idx)
        
        
        df_inno = pd.DataFrame(align_dict['inno'][1][:,finded_idx-2:finded_idx+3])
        df_inno['canon'] = pd.DataFrame(align_dict['inno'][1][:,finded_idx])
        
        df_inno['sp'] = align_dict['inno'][0]

        df_noninno = pd.DataFrame(align_dict['non_inno'][1][:,finded_idx-2:finded_idx+3])
        df_noninno['canon'] = pd.DataFrame(align_dict['non_inno'][1][:,finded_idx])
        
        df_noninno['sp'] = align_dict['non_inno'][0]

        df_all = pd.concat([df_inno, df_noninno])
        
        df_all['sp'] = df_all['sp'].apply(lambda x: x.split('.')[1])
        df_all.to_csv('chrom_int/{}_{}.tsv'.format(chrom_int, idx), sep = '\t', index=False)
        return get_annotation(inno_array, noninno_array, idx, inno_exept, noninno_exept)
    
    
chrom_int = argv[1] #'NC_044238.2'
df = pd.read_csv('positions_with_genes.tsv', sep = '\t')
df1 = df[df['chrom']==chrom_int]
coords = np.unique(df1['coord'].to_numpy())

file_path = 'maf_by_chrom_big/{}.maf'.format(chrom_int)
multiple_alignments = []

for multiple_alignment in AlignIO.parse(file_path, "maf"):
    
    seqrecs = []
    
    for seqrec in multiple_alignment:
        
        seqrec.annotations["start"]
        seqrecs.append((str(seqrec.seq), seqrec.name, seqrec.annotations["start"], seqrec.annotations["size"]))
        
        if "2_bTaeGut1" in seqrec.name:
            start = seqrec.annotations["start"]
            length = seqrec.annotations["size"]
            
    coords_which_fit = (coords < start+length)&(coords >= start)
    
    if coords_which_fit.sum() > 0:
        
        idxs_coords = coords[((coords < start+length)&(coords >= start))]
        
        multiple_alignments.append(get_df_with_counts(seqrecs, coords[coords_which_fit], chrom_int))
        print(multiple_alignments[-1])
    

table = pd.DataFrame(multiple_alignments)
table['chrom'] = chrom_int
table.to_csv('chrom_int_anno/{}.csv'.format(chrom_int), index = False)
