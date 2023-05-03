#server
sbatch -p vgl bird_innovation/scripts/permutation_test/launch_get_list_1.sh
tar -zcvf permutation_test_vcf.gz permutation_test_vcf/
#local
#scp  adenisova@login04-hpc.rockefeller.edu:/vggpfs/fs3/vgl/store/adenisova/data/innovation/branch_analysis/test_october/test_gerp/coursework_results/permutation_test_vcf.gz ~/Desktop/coursework/data/final_data/
sh launch_bash_snpeff.sh
get_list_of_genes.ipynb
#scp
unzip dir_gene_list.zip
rm dir_gene_list.zip 