#!/bin/bash

wig=$1
main_dir=$2
final_wig="${main_dir}/${wig}_final"

wig="${main_dir}/${wig}"

mkdir -p $final_wig

for dir in $(ls $wig)
do
	mkdir -p $final_wig/$dir
	
	for file in $(ls $wig/$dir)
	do
		grep -v 'fixedStep' $wig/$dir/$file | tail -n+2 > $final_wig/$dir/$file

		file_index="${file}_index"
		final_result="${file}_final"

		grep 'fixedStep' $wig/$dir/$file | cut -d' ' -f3 | cut -d'=' -f2 > coordinate 
		tail -n+2 $wig/$dir/$file | awk '/fixedStep/ {if (count) print count; print; count=0; next} {count++} END {print count}' \
		| awk 'NR % 2 ==0' > number_of_letters

		touch $final_wig/$dir/$file_index

		paste coordinate number_of_letters > for_index.txt
		rm coordinate number_of_letters
		
		less for_index.txt | while read -r coordinate number_of_letters
			do
				number_of_letters="$(($number_of_letters+$coordinate-1))"
				seq $coordinate $number_of_letters >> $final_wig/$dir/$file_index
			done

		paste $final_wig/$dir/$file_index $final_wig/$dir/$file > $final_wig/$dir/$final_result

		rm $final_wig/$dir/$file_index
		rm $final_wig/$dir/$file
	done
done 






