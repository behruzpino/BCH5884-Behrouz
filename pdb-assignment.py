#!/usr/local/bin/python3
#Behrouz Ghazi Esfahani

import sys


pdbname=sys.argv[1]
f=open(pdbname,'r')
lines=f.readlines()

atomlist=[]

for line in lines:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  atomlist.append(line_list)
  
  
f.close()

with open('new_file_for_atoms.pdb', 'w') as f:
    for item in atomlist:
        f.write("%s\n" % item)





print ("DOne")
