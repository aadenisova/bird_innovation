#!/bin/bash

dir=$1
file=$2

cd /Users/aleksandradenisova/programs/snpEff

java -Xmx8g -jar snpEff.jar -v bTaeGut1.4.pri ~/Desktop/coursework/data/$dir/$file > $file.ann
mv snpEff_summary.html $file.html
mv snpEff_genes.txt $file.txt

cp $file.ann $file.html $file.txt ~/Desktop/coursework/data/final_data/ 
