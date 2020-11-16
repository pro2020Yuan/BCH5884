#!/usr/bin/env python3
#https://github.com/pro2020Yuan/bch5844.git

import matplotlib.pyplot as plt

import numpy as np

#open the file and creat lists of x and y values
f=open("superose6_50.asc")
lines=f.readlines()
f.close()

t=[]
vector=[]
for line in lines[3:]:
	words=line.split()
	try:
		t.append(float(words[0]))
		vector.append(float(words[1]))
	except:
		print ("could not parse", line)
		continue
    
# make the list to arrays and then plot
t=np.array(t)
vector=np.array(vector)
plt.plot(t,vector)
plt.xlim(0,180)
plt.ylim(0,1200)

plt.show()

# get the troughs by determining the point value less than both neighbors
# the 1st and last points only compare with their one neighbor
collection_of_boundary = []

for i in range(0,(len(vector))):
    if((i==0 and vector[i+1]>vector[i])or(i==(len(vector)-1) and vector[i-1]>vector[i]) ):
        collection_of_boundary.append([('position: ',i),('value: ',vector[i])])
    
    elif((vector[i-1]>vector[i] and vector[i+1]>vector[i])):
        
        collection_of_boundary.append([('position: ',i),('value: ',vector[i])])
        

# get the peaks by determing the max position between two neighbouring troughs
collection_of_peak = []


for i in range(0,(len(collection_of_boundary))):
    
    if(i != (len(collection_of_boundary)-1)):
        #the argmax returns to the position in the specific numpy array, so the real position has to add the left boundary of the range
        position_of_peak = collection_of_boundary[i][0][1] + np.argmax(vector[(collection_of_boundary[i][0][1]):(collection_of_boundary[i+1][0][1])])
        print('peak',i+1,'begins at time ',t[collection_of_boundary[i][0][1]],' and ends at time ',t[collection_of_boundary[i+1][0][1]])
        print('peak',i+1,'time is: ', t[position_of_peak])
        print('peak',i+1,'absorbance value is: ',vector[position_of_peak])
        print("")