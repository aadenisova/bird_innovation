source /vggpfs/fs3/vgl/store/adenisova/anaconda3/etc/profile.d/conda.sh 
conda activate ncbi_datasets

for genome in $(awk '{print $1}' genomes_id.txt)
do
    echo $genome
    datasets download genome accession $genome 
    unzip ncbi_dataset.zip 
    cp -r ncbi_dataset/data/$genome genomes
    rm ncbi_dataset.zip
    rm -r ncbi_dataset
    rm README.md
done

