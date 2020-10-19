#!/usr/bin/env python3
#Yuan Liu
import sys

f=open("2FA9noend.pdb")
lines=f.readlines()

sumx=0
sumy=0
sumz=0
summ=0
gsumx=0
gsumy=0
gsumz=0

gelist=[]
gelist2=[]
gelist3=[]
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

x=input("Please make a choice by entering center of mass or geometric center: ")
      
if x == "center of mass":
    for line in lines:
      words=line.split()
      words[1]=int(words[1])
      words[5]=int(words[5])
      words[6]=float(words[6])
      words[7]=float(words[7])
      words[8]=float(words[8])
      gsumx=gsumx+words[6]
      gsumy=gsumy+words[7]
      gsumz=gsumz+words[8]      
      words[9]=float(words[9])
      words[10]=float(words[10])
      words[6]=round(words[6]-gsumx/len(lines),3)
      words[7]=round(words[7]-gsumy/len(lines),3)
      words[8]=round(words[8]-gsumz/len(lines),3)
      gelist2.append(words)
    f.close()
    f=open("OCT18.out",'w')
    for atom in gelist2:
      s="{0:6s}{1:5d}  {2:4s}{3:3s} {4:1s}{5:4d}    {6:8.3f}{7:8.3f}{8:8.3f}{9:6.2f}{10:6.2f}           {11:2s}  \n"
      f.write(s.format(atom[0],atom[1],atom[2],atom[3],atom[4],atom[5],atom[6],atom[7],atom[8],atom[9],atom[10],atom[11]))
    f.close()
    
    
elif x == "geometric center":	
    for line in lines:
      words=line.split()
      words[1]=int(words[1])
      words[5]=int(words[5])
      words[6]=float(words[6])
      words[7]=float(words[7])
      words[8]=float(words[8])
      words[9]=float(words[9])
      words[10]=float(words[10])
      
      if words[11]=="N":

          sumx=sumx+words[6]*14.0067
          sumy=sumy+words[7]*14.0067
          sumz=sumz+words[8]*14.0067
          summ=summ+14.0067

      elif words[11]=="C":
          
          sumx=sumx+words[6]*12.0107
          sumy=sumy+words[7]*12.0107
          sumz=sumz+words[8]*12.0107
          summ=summ+12.0107

      elif words[11]=="S":
          
          sumx=sumx+words[6]*32.065
          sumy=sumy+words[7]*32.065
          sumz=sumz+words[8]*32.065
          summ=summ+32.065

      else:
          
          sumx=sumx+words[6]*15.999
          sumy=sumy+words[7]*15.999
          sumz=sumz+words[8]*15.999
          summ=summ+15.999
         
      words[6]=round(words[6]-sumx/summ,3)
      words[7]=round(words[7]-sumy/summ,3)
      words[8]=round(words[8]-sumz/summ,3)
      gelist3.append(words)
    f.close()
    f=open("OCT18.out",'w')
    for atom in gelist3:
      s="{0:6s}{1:5d}  {2:4s}{3:3s} {4:1s}{5:4d}    {6:8.3f}{7:8.3f}{8:8.3f}{9:6.2f}{10:6.2f}           {11:2s}  \n"
      f.write(s.format(atom[0],atom[1],atom[2],atom[3],atom[4],atom[5],atom[6],atom[7],atom[8],atom[9],atom[10],atom[11]))
    f.close()

else:

    print("Your option is non-existed!")