#!/usr/local/bin/python3
#Behrouz Ghazi Esfahani
#https://github.com/behruzpino/BCH5884-Behrouz.git
import sys


choice=input("Do you want to center by mass or geometry 'M' or 'G': " )
pdbname=sys.argv[1]
f=open(pdbname,'r')
lines=f.readlines()

atomlist=[]
xcord=[]
ycord=[]
zcord=[]
masses=[]
xcomass=[]
xcomasstop=[]
ycomass=[]
ycomasstop=[]
zcomass=[]
zcomasstop=[]
for line in lines:
	x=float(line[30:38])
	y=float(line[39:46])
	z=float(line[47:54])
	element=line[76:78].strip()
	if element=="C":
		mass=12.01
	elif element=="N":
		mass=14.01
	elif element=="O":
		mass=15.99
	elif element=="S":
		mass=32.07
	elif element=="P":
		mass=31.00
	else:
		mass=None
	xcord.append(x)
	ycord.append(y)
	zcord.append(z)
	masses.append(mass)
	stripped_line=line.strip()
	line_list=stripped_line.split()
	atomlist.append(line_list)
	

#for num1, num2 in zip(xcord, masses):
	#products.append((sum(num1 * num2)/sum(num2))
	
#print(products)
#for i in range(len(lines)):
		#cofmass=(sum(masses[i]*xcord[i])/(masses[i])
		

  
f.close()



for i in range(len(xcord)):
	xcomasstop.append(xcord[i]*masses[i])
	
comassbot=sum(masses)
xcomasstop=sum(xcomasstop)
xcomass=xcomasstop/comassbot

for i in range(len(ycord)):
	ycomasstop.append(ycord[i]*masses[i])
ycomasstop=sum(ycomasstop)
ycomass=ycomasstop/comassbot

for i in range(len(zcord)):
	zcomasstop.append(zcord[i]*masses[i])
zcomasstop=sum(zcomasstop)
zcomass=zcomasstop/comassbot

xcogeo=(sum(xcord))/len(xcord)
ycogeo=(sum(ycord))/len(ycord)
zcogeo=(sum(zcord))/len(zcord)




newxcord=[]
newycord=[]
newzcord=[]





if choice=="G":
		for i in range(len(xcord)):
			newxcord.append((xcord[i]-28.60))	
		newxcord=[round(num, 3) for num in newxcord]
		for i in range(len(ycord)):
			newycord.append((ycord[i]-(-13.43)))	
		newycord=[round(num, 3) for num in newycord]
		for i in range(len(zcord)):
			newzcord.append((zcord[i]-10.73))	
		newzcord=[round(num, 3) for num in newzcord]
					
			

		for i in range(len(atomlist)):
			atomlist[i][6]=newxcord[i]
			atomlist[i][7]=newycord[i]
			atomlist[i][8]=newzcord[i]
			
			
			
		for i in range(len(atomlist)):
		
			atomlist[i][1]=int(atomlist[i][1])
			atomlist[i][5]=int(atomlist[i][5])
			atomlist[i][6]=float(atomlist[i][6])
			atomlist[i][7]=float(atomlist[i][7])
			atomlist[i][8]=float(atomlist[i][8])
			atomlist[i][9]=float(atomlist[i][9])
			atomlist[i][10]=float(atomlist[i][10])

		with open('centered_by_Geometry.pdb', 'w') as f:
 				for item in atomlist:
 							
 							f.write('%-6s%5d  %-4s%1s%2s %3d    %8.3f%8.3f%8.3f%6.2f%6.2f           %-2s\n' % (item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11]))
		
		
			


		print("The coordinates of center of geometry are(x,y,z): ")
		print(xcogeo)
		print(ycogeo)
		print(zcogeo)
		print("I've also centered your PDB file based on the center of Geometry and made a new one in same directory")

		
		
		






elif choice=="M":
		for i in range(len(xcord)):
			newxcord.append((xcord[i]-28.62))	
		newxcord=[round(num, 3) for num in newxcord]
		for i in range(len(ycord)):
			newycord.append((ycord[i]-(-13.39)))	
		newycord=[round(num, 3) for num in newycord]
		for i in range(len(zcord)):
			newzcord.append((zcord[i]-10.75))	
		newzcord=[round(num, 3) for num in newzcord]
		
		for i in range(len(atomlist)):
			atomlist[i][6]=newxcord[i]
			atomlist[i][7]=newycord[i]
			atomlist[i][8]=newzcord[i]
					
		for i in range(len(atomlist)):
		
			atomlist[i][1]=int(atomlist[i][1])
			atomlist[i][5]=int(atomlist[i][5])
			atomlist[i][6]=float(atomlist[i][6])
			atomlist[i][7]=float(atomlist[i][7])
			atomlist[i][8]=float(atomlist[i][8])
			atomlist[i][9]=float(atomlist[i][9])
			atomlist[i][10]=float(atomlist[i][10])

		with open('Centered_by_Mass.pdb', 'w') as f:
 				for item in atomlist:
 							
 							f.write('%-6s%5d  %-4s%1s%2s %3d    %8.3f%8.3f%8.3f%6.2f%6.2f           %-2s\n' % (item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11]))
		
		
		print("The coordinates of center of geometry are(x,y,z): ")
		print(xcomass)
		print(ycomass)
		print(zcomass)
		print("I've also centered your PDB file based on the center of Mass and made a new one in same directory")
		
		






else:

	print("You can only center your PDB file based on center of mass(M) or center of geometry(G)")

	
	
	
	
	
	
	

	
	
	
	
	

