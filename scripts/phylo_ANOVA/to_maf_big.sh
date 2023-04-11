#!/bin/bash

ref_genome=$1
ref_seq=$2
output=$3
input_align=$4

hal2maf --onlyOrthologs --noDupes --refGenome $ref_genome --refSequence \
$ref_seq $input_align $output
