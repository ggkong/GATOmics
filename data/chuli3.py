

import pandas as pd

# 假设您已经将0.8.go.tsv和P.txt文件读取到DataFrame中
# 读取P.txt中的基因名字
p_df = pd.read_csv('D:\\网页下载\\MRNGCN-master\\MRNGCN-master\\preProcessing\\p.txt', header=None, sep='\t')
gene_names = p_df[1].tolist()

# 读取邻接矩阵文件
adjacency_matrix = pd.read_csv('D:\\网页下载\\MRNGCN-master\\MRNGCN-master\\data\\0.8.exp.tsv', sep='\t', index_col=0)

# 初始化新的邻接矩阵，缺失的数据用0填充
new_adjacency_matrix = pd.DataFrame(0, index=gene_names, columns=gene_names)

# 填充新邻接矩阵
for gene1 in gene_names:
    for gene2 in gene_names:
        if gene1 in adjacency_matrix.index and gene2 in adjacency_matrix.columns:
            new_adjacency_matrix.at[gene1, gene2] = adjacency_matrix.at[gene1, gene2]

# 保存新的邻接矩阵到CSV文件
new_adjacency_matrix.to_csv('new_adjacency_matrix.csv')
