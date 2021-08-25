
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# visualize vis in coding gene, non coding gene, intergenic regions
vis_gene = pd.DataFrame({'position' : ["coding gene", "non-coding gene", "intergenic regions"], 'number':[21, 1202, 132]})
vis_gene_plot = sns.barplot(x="position", y="number", data=vis_gene)
plt.show()


# distribution of length of gene
# gene with vis
# convert bed format to pd.dataframe
gene_vis_df = pd.read_csv('gene_vis.bed', sep='\t', header=None)
header = ['Chrom', 'Start', 'End']
gene_vis_df.columns = header[:len(gene_vis_df.columns)]
# calculate the gene length as the 3rd column
gene_vis_df["length"] = gene_vis_df["End"] - gene_vis_df["Start"]

# gene w/o vis
gene_wo_vis_df = pd.read_csv('gene_wo_vis.bed', sep='\t', header=None)
gene_wo_vis_df.columns = header[:len(gene_wo_vis_df.columns)]
gene_wo_vis_df["length"] = gene_wo_vis_df["End"] - gene_wo_vis_df["Start"]

# create new dataframe for plotting
vis_plot_df = pd.DataFrame({'kind' : 'gene_vis', 'length': gene_vis_df["length"]})
vis_wo_plot_df = pd.DataFrame({'kind' : 'gene_wo_vis', 'length': gene_wo_vis_df["length"]})
vis_comb_plot_df = pd.concat([vis_plot_df, vis_wo_plot_df], axis=0)

# plot
sns.displot(data=vis_comb_plot_df, x='length', log_scale=True, hue='kind', stat="density", common_norm=False)
    # hue: show two subgroups in one figure
    # col: show two subgp in diff figure
    # w/o stat: count
    # default common_norm: normalize by the entire gp
plt.show()
sns.displot(data=vis_comb_plot_df, x='length', log_scale=True, col='kind')
plt.show()


# visualize vis in coding gene, non coding gene, intergenic regions
vis_protcod_gene = pd.DataFrame({'position' : ["utr", "intron", "exon"], 'number':[57, 1999, 144]})
vis_protcod_plot = sns.barplot(x="position", y="number", data=vis_protcod_gene)
plt.show()