#!/usr/bin/env python3
#https://github.com/pro2020Yuan/BCH5884.git
import numpy as np
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import seaborn as sns
from scipy.stats import ttest_ind

# find those significantly differentially expressed miRNAs as data for plotting
def findqualifydata(filename):
    f=open(filename)
    lines=f.readlines()
    data_len = len(lines)
    f.close()

    miRNA_ID=[]
    words = []
    control_exp = []
    ID_fold = []

    for line in lines[3:-1]:
        words=line.split(',')
# calculate p value
        pop1 = np.array([float(words[1]),float(words[2])])
        pop2 = np.array([float(words[3]),float(words[4])])
        t_value,p_value = ttest_ind(pop1,pop2,equal_var=False)
# screen qualified data
        if (((float(words[5]) > 2) or (float(words[5]) < 0.5)) and (p_value<0.05)):
            miRNA_ID.append(words[0])
            control_exp.append([float(words[1]),float(words[2]),float(words[3]),float(words[4])])
            ID_fold.append([words[0],float(words[5])])
    return miRNA_ID, control_exp, ID_fold,data_len

# call the function to read file
miRNA_ID, control_exp, ID_fold, data_len=findqualifydata("sequencing.csv")    

# Show and count for upregulated, downregulated, and undifferentially expressed miRNA numbers
up = 0
down = 0
undifferentiate = 0
up_ID = []
down_ID = []
for i in range(0,len(ID_fold)):
    if (float(ID_fold[i][1]) > 2):
        up +=1
        up_ID.append(ID_fold[i][0])
    elif (float(ID_fold[i][1]) < 0.5):
        down +=1
        down_ID.append(ID_fold[i][0])
print ("There are",up,"upregulated miRNAs:",up_ID,"and",down,"downregulated miRNAs:",down_ID)

# select top 5 upregulated miRNAs as candidates for target mRNA screening in databases
ID_fold= sorted(ID_fold,key=lambda x: x[1],reverse=True)
top5 = []
time = 1
for i in ID_fold:
    if ((i[1] > 2) and (time <=5)):
        top5.append(i)
        time+=1
print ("The top 5 upregulated miRNAs are", top5,"Please find their mRNA targets on TargetScan.org.")

# calculation for Venn Diagram plotting
undifferentiate = data_len-up-down
up= up + undifferentiate
donw = down + undifferentiate

# default heatmap: just a visualization of this square matrix
# creat the dataset for generating a heatmap
control_exp = np.array(control_exp)

fig, ax = plt.subplots(figsize=(5,12),dpi=144)
sns.heatmap(control_exp,vmin=0, vmax=1,center=0.4,xticklabels=["donor1 2D","donor2 2D","donor1 3D","donor2 3D"],yticklabels=miRNA_ID,cmap="PiYG")
ax.set_title('Heatmap of miRNAs expression level in different EVs')
txt = '''
      Figure 1. The heatmap for differentially
      expressed EV miRNAs sequencing data from
      2D and 3D cell culture system.The sequencing
      data was generated from NovaSeq6000.'''
fig.text(-0.25,0.01,txt, fontsize=18)
plt.savefig("heatmap.png",dpi=144, bbox_inches='tight')

plt.figure()
fig1, ax1 = plt.subplots(figsize=(5,5),dpi=144)
# 2 group Venn diagram:
venn2(subsets = (up, down, undifferentiate), set_labels = ('Upregulated', 'Downregulated'))
plt.title("Venn Diagram")
txt = '''
      Figure 2. The Venn Diagram for differentially expressed EV 
      miRNAs sequencing data from 2D and 3D cell culture system.
      Left represented upregulated, right represented downregulated,
      and the intersection was the undifferentiated.'''
fig1.text(0.05,-0.1,txt)
plt.savefig("Venn Diagram.png",dpi=144, bbox_inches='tight')


