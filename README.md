# Visualization

Use bedtools to get the overlaps between HIV-vis bed file and other gene annotation files.
command lines in the terminal:

Workflow:
1. sort the files uniquely to remove the repeat data by sort -u and save as file.sort.bed
2. sort the files according to the start position by sort -k2n and save as file.sortu.bed
3. harmonize the files format: the format of the gene annotation files is different from the HIV-vis file. 
gene annotation file: 
17 start end
HIV-vis file:
chr17 start end
adding "chr" for the gene annotation files (save as file.chr.bed) and conduct bedtools intersect

for visualize HIV integration region: 
1. check the overlaps and count the number: bedtools intersect -wa -a HIV_vis_str.bed -b gene annotation.bed | sort -u | wc -l
2. run task2.py and plot the figure. 

for the distribution figure: 
1. find the overlap part between gene and HIV-vis (or find the part without any overlaps) and save outputs as files. 
bedtools intersect -wa -a gene annotation.bed -b HIV_vis_str.bed | sort -u > gene_vis.bed
bedtools intersect -wa -v -a gene annotation.bed -b HIV_vis_str.bed | sort -u > gene_wo_vis.bed
2. run task2.py to convert the bed format to pandas dataframe, calculate the gene length, and plot the figures. 
