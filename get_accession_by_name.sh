IFS=''
cat all_sp_names_from_db.tsv | while read line; do datasets summary genome taxon "$line" | python3 get_accesion_by_name.py a $line; done
