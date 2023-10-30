#!/bin/bash

for num in {1..35}
do
sh bash_snpEff.sh final_data/permutation_test_vcf positions_for_8_${num}.vcf final_data/permutation_anno 2> ~/Desktop/coursework/data/final_data/permutation_anno/zibra_${num}.log
done
