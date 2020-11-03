#!/usr/bin/env python3
# https://github.com/pro2020Yuan/bch5844.git
import sys, math

def readpdb(pdbname):
	f=open(pdbname)
	lines=f.readlines()
    
	records=[]
	for line in lines:
		if line[:4]=="ATOM" or line[:6]=="HETATM":
			d={}
			d['rtype']=line[0:6]
			d['atomnumber']=int(line[6:11])
			d['atomtype']=line[12:16]
			d['altloc']=line[16:17]
			d['residue']=line[17:20]
			d['chain']=line[21:22]
			d['residuenumber']=int(line[22:26])
			d['icode']=line[26:27]
			d['x']=float(line[30:38])
			d['y']=float(line[38:46])
			d['z']=float(line[46:54])
			d['occupancy']=float(line[54:60])
			d['tempfact']=float(line[60:66])
			d['element']=line[76:78].strip()
			d['charge']=line[78:80].strip()
			records.append(d)
	
	return records

l1=readpdb("2FA9noend.pdb")	
l2=readpdb("2FA9noend2mov.pdb")
print ("l1=",l1)
print ("l2=",l2)

def findRMSD():	
	number1=len(l1)

	vn=0
	for n1,n2 in zip(l1,l2):
		vn+=(n1['x']-n2['x'])**2+(n1['y']-n2['y'])**2+(n1['z']-n2['z'])**2
	vn=math.sqrt(vn/number1)
	return vn
RMSD=findRMSD()
print(RMSD)