from Bio import AlignIO
import numpy as np
import pandas as pd
from sys import argv

file_path = argv[1]#'../../data/stage2/NC_044224.2.maf'

list_inno = ["1_bSylAtr1", "1_bGeoTri1", "4_bAquChr1", "1_bSteHir1"]
list_noninno = ["1_bSylBor1", "2_bTaeGut1", "1_bBucAby1", "1_bAlcTor1"]


def is_in_list(name, list_of):
    ans = False
    for bird in list_of:
        if bird in name:
            ans = True
    return ans  



def check(matrix, num):
    
    return np.array([(matrix[:,num] == 'A').sum(),
                     (matrix[:,num] == 'T').sum(),
                     (matrix[:,num] == 'G').sum(),
                     (matrix[:,num] == 'C').sum(),
                    ]), np.array([(matrix[:,num] == 'N').sum(),
                     (matrix[:,num] == '-').sum()])


def get_df_with_counts(align):

    align_dict = {'inno':[], 'non_inno': []}

    for seqreq in align:

        sequence = [*(seqreq[0].upper())]

        if is_in_list(seqreq[1], list_inno):

            align_dict['inno'].append(sequence)

        elif is_in_list(seqreq[1], list_noninno):

            align_dict['non_inno'].append(sequence)
            if "2_bTaeGut1" in seqreq[1]:
                start = seqreq[2]
                length = seqreq[3]


    align_dict['inno'] = np.matrix(align_dict['inno'])
    align_dict['non_inno'] = np.matrix(align_dict['non_inno'])
    
    list_of = np.array(['A', 'T', 'G', 'C'])   

    new_list = []
    n=0
    for i in range(length):

        inno_array, inno_exept = check(align_dict['inno'], i)
        noninno_array, noninno_exept = check(align_dict['non_inno'], i)


        max_inno = inno_array.sum()
        max_noninno = noninno_array.sum()
        
        if (max_inno>=3) and (max_noninno >=3):

            cons = (bool((inno_array==max_inno).sum() and (noninno_array==max_noninno).sum()) 
            & (inno_array.argmax() != noninno_array.argmax()))

            inno = (cons==False) and (bool((inno_array==max_inno).sum()) and noninno_array[inno_array.argmax()]==0)

            non_inno = (cons==False) and (bool((noninno_array==max_noninno).sum()) and inno_array[noninno_array.argmax()]==0)

            new_list.append([start+n, 
                             cons, 
                             inno, 
                             non_inno, 
                            ','.join(list(list_of[inno_array!=0])),
                            ','.join(list(list_of[noninno_array!=0])), 
                            max_inno,
                            max_noninno,
                            max_inno+max_noninno,
                            inno_exept[0],
                            inno_exept[1],
                            noninno_exept[0],
                            noninno_exept[1]])
        n+=1

    df = pd.DataFrame(new_list, columns=['start', 'cons', 'inno', 'non_inno', 'Ref_inno', 'Alt_noninno',
                                         'n_inno', 'n_noninno', 'n', 'inno_N', 'inno_-', 'noninno_N', 'noninno_-'])
    return df





multiple_alignments = []
for multiple_alignment in AlignIO.parse(file_path, "maf"):
    
    seqrecs = []
    
    for seqrec in multiple_alignment:
        
        seqrecs.append((str(seqrec.seq), seqrec.name, seqrec.annotations["start"], seqrec.annotations["size"]))
    
    if len(seqrecs) >= 6:
        
        multiple_alignments.append(get_df_with_counts(seqrecs))

        

table = pd.concat(multiple_alignments)
table.to_csv('maf_counts/{}.csv'.format(file_path.split('/')[-1]), index = False)
    