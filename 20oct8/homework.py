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

print(gelist)
f.close()

f=open("OCT12.out",'w')
for n in gelist:
    s="{}\n" 
    f.write(s.format(n))
f.close()