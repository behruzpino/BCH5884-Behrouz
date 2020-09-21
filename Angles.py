#!/usr/local/bin/python3
#https://github.com/behruzpino/BCH5884-Behrouz.git
import math

xA=8
xB=13
xC=53

yA=4
yB=-32
yC=102

dxAB=xA-xB
dxAC=xA-xC
dxBC=xB-xC

dyAB=yA-yB
dyAC=yA-yC
dyBC=yB-yC

dAB=math.sqrt(dxAB**2+dyAB**2)
dAC=math.sqrt(dxAC**2+dyAC**2)
dBC=math.sqrt(dxBC**2+dyBC**2)

dABs=dAB**2
dACs=dAC**2
dBCs=dBC**2

Alpha=math.acos((dACs+dABs-dBCs)/(2*dAC*dAB))
Betta=math.acos((dBCs+dABs-dACs)/(2*dAB*dBC))
Gamma=math.acos((dBCs+dACs-dABs)/(2*dAC*dBC))

Alpha=Alpha*180/math.pi
Betta=Betta*180/math.pi
Gamma=Gamma*180/math.pi

print(Alpha)
print(Betta)
print(Gamma)

print(dAB)
print(dBC)
print(dAC)

