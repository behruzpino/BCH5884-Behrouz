#!/usr/local/bin/python3
#Behrouz Ghazi Esfahani
#https://github.com/behruzpino/BCH5884-Behrouz.git
import sys

def readpdb(pdbname1,pdbname2):
	
	f1=open(pdbname1,'r')
	f2=open(pdbname2,'r')

	lines1=f1.readlines()
	lines2=f2.readlines()

	atomlist1=[]
	xcord1=[]
	ycord1=[]
	zcord1=[]


	for line in lines1:
			x1=float(line[30:38])
			y1=float(line[39:46])
			z1=float(line[47:54])
	
			xcord1.append(x1)
			ycord1.append(y1)
			zcord1.append(z1)
	
	
			stripped_line1=line.strip()
			line_list1=stripped_line1.split()
			atomlist1.append(line_list1)
	
	
	atomlist2=[]
	xcord2=[]
	ycord2=[]
	zcord2=[]


	for line in lines2:
		if line[:4]=="ATOM":
	
			x2=float(line[30:38])
			y2=float(line[39:46])
			z2=float(line[47:54])

			xcord2.append(x2)
			ycord2.append(y2)
			zcord2.append(z2)

			stripped_line2=line.strip()
			line_list2=stripped_line2.split()
			atomlist2.append(line_list2)
	


def rsmd(list1,list2):
        rsmd_number=0
	for i in range(0, len(atomlist1)):
		xdev=((xcord1[i]-xcord2[i])**2)
		ydev=((ycord1[i]-ycord2[i])**2)
		zdev=((zcord1[i]-zcord2[i])**2)
	rsmd_number=((xdev+ydev+zdev)/len(atomlist1))**0.5

if __name__=="__main__":
	readpdb(sys.arg[1], sys.arg[2])
	rsmd_number(atomlist1, atomlist2)
	print(rsmd_number)
		











