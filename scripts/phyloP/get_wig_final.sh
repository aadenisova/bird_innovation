#!/bin/bash

model=$1
maf=$2
result=$3
method=$4
dir_to_write=$5
output_format=$6
dir_to_make=$7

#mkdir -p $dir_to_make/$dir_to_write

phyloP --method $method --mode CON $output_format $model $maf > $dir_to_make/$dir_to_write/$result
