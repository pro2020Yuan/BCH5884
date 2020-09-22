#!/usr/bin/env python3
import math

YA=int(input("Please enter the Y coordinates for point A: "))
XA=int(input("Please enter the X coordinates for point A: "))
YB=int(input("Please enter the Y coordinates for point B: "))
XB=int(input("Please enter the X coordinates for point B: "))
YC=int(input("Please enter the Y coordinates for point C: "))
XC=int(input("Please enter the X coordinates for point C: "))

a=math.sqrt((XB-XC)**2+(YB-YC)**2)
b=math.sqrt((XA-XC)**2+(YA-YC)**2)
c=math.sqrt((XA-XB)**2+(YA-YB)**2)

cosA=(c**2+b**2-a**2)/(2*b*c)

A=math.acos(cosA)*180/math.pi

print(A)