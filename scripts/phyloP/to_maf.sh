#!/bin/bash
ref_genome=$1
ref_seq=$2
sp=$3
output=$4
input_align=$5

hal2maf --onlyOrthologs --noDupes --refGenome $ref_genome --refSequence \
$ref_seq --targetGenomes $sp $input_align $output

