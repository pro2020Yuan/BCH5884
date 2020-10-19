#!/usr/bin/env python3
#Yuan Liu
import sys

f=open("2FA9noend.pdb")
lines=f.readlines()

gelist=[]
for line in lines:
      words=line.split()
      words[1]=int(words[1])
      words[5]=int(words[5])
      words[6]=float(words[6])
      words[7]=float(words[7])
      words[8]=float(words[8])
      words[9]=float(words[9])
      words[10]=float(words[10])
      gelist.append(words)

print("l=",gelist)
f.close()
f=open("OCT12.out",'w')
for atom in gelist:
    
    s="{0:6s}{1:5d}  {2:4s}{3:3s} {4:1s}{5:4d}    {6:8.3f}{7:8.3f}{8:8.3f}{9:6.2f}{10:6.2f}           {11:2s}  \n"
    f.write(s.format(atom[0],atom[1],atom[2],atom[3],atom[4],atom[5],atom[6],atom[7],atom[8],atom[9], atom[10],atom[11]))
f.close()
