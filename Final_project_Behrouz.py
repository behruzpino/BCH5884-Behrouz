#!/usr/bin/python3
#Behrouz Ghazi Esfahani	
#https://github.com/behruzpino/BCH5884-Behrouz.git



import math 
import sys
import matplotlib.pyplot as plt
import numpy as np

def Rg(filename):
	'''
	Calculates the Radius of Gyration (Rg) of a protein given its .pdb 
	structure file. Returns the Rg integer value in Angstrom.
	'''
	coord = list()
	mass = list()
	Structure = open(filename, 'r')
	for line in Structure:
		try:
			line = line.split()
			x = float(line[6])
			y = float(line[7])
			z = float(line[8])
			coord.append([x, y, z])
			if line[-1] == 'C':
				mass.append(12.0107)
			elif line[-1] == 'O':
				mass.append(15.9994)
			elif line[-1] == 'N':
				mass.append(14.0067)
			elif line[-1] == 'S':
				mass.append(32.065)
		except:
			pass
	xm = [(m*i, m*j, m*k) for (i, j, k), m in zip(coord, mass)]
	tmass = sum(mass)
	rr = sum(mi*i + mj*j + mk*k for (i, j, k), (mi, mj, mk) in zip(coord, xm))
	mm = sum((sum(i) / tmass)**2 for i in zip(*xm))
	rg = math.sqrt(rr / tmass-mm)
	return(round(rg, 3))


#coulmns
Superose_6_10_300_GL=[10, 70, 9, 24, 5, 5000]
Superose_6_5_300_GL=[10, 70, .8, 3, 5, 5000]
Superose_6_3_300_GL=[10, 70, .7, 2.4, 5, 5000]
HiPrep_16_60_Sephacryl_S_100=[5, 30, 30, 120, 1, 100]
HiPrep_26_60_Sephacryl_S_100=[5, 30, 50, 320, 1, 100]
HiPrep_16_60_Sephacryl_S_200=[10, 50, 30, 120, 5, 250]
HiPrep_26_60_Sephacryl_S_200=[10, 50, 50, 320, 5, 250]
HiPrep_16_60_Sephacryl_S_300=[15, 100, 30, 120, 10, 1500]
HiPrep_26_60_Sephacryl_S_300=[15, 100, 50, 320, 10, 1500]
HiPrep_16_60_Sephacryl_S_400=[20, 150, 30, 120, 20, 8000]
HiPrep_26_60_Sephacryl_S_400=[20, 150, 50, 320, 20, 8000]





if __name__ == '__main__':
	Rg_pro=Rg(sys.argv[1])
	print('Radius of Gyration is: ' + str(Rg_pro))
	
	
print('1. Superose_6_10_300_GL')
print('2. Superose_6_5_300_GL')
print('3. Superose_6_3_300_GL')
print('4. HiPrep_16_60_Sephacryl_S_100')
print('5. HiPrep_26_60_Sephacryl_S_100')
print('6. HiPrep_16_60_Sephacryl_S_200')
print('7. HiPrep_26_60_Sephacryl_S_200')
print('8. HiPrep_16_60_Sephacryl_S_300')
print('9. HiPrep_26_60_Sephacryl_S_300')
print('10. HiPrep_16_60_Sephacryl_S_400')
print('11. HiPrep_26_60_Sephacryl_S_400')







choice = input("Enter column number:")
print("Column is: " + choice)

c1 = []

if choice == str(1):
	c1 = Superose_6_10_300_GL
elif choice == str(2):
	c1 = Superose_6_5_300_GL
elif choice == str(3):
	c1 = Superose_6_3_300_GL
elif choice == str(4):
	c1 = Superose_6_3_300_GL
elif choice == str(5):
	c1 = Superose_6_3_300_GL
elif choice == str(6):
	c1 = Superose_6_3_300_GL
elif choice == str(7):
	c1 = Superose_6_3_300_GL
elif choice == str(8):
	c1 = Superose_6_3_300_GL	
elif choice == str(9):
	c1 = Superose_6_3_300_GL	
elif choice == str(10):
	c1 = Superose_6_3_300_GL	
elif choice == str(11):
	c1 = Superose_6_3_300_GL	
else:
	print("Please enter the column index you want to use, Like: 1")
	

normalized_Rg = (Rg_pro-c1[0])/(c1[1]-c1[0])

#print(c1)
#print(normalized_Rg)
print("The radius of gyration for this protein is ", Rg_pro, "A")

x = c1[2] + ((c1[3] - c1[2])*normalized_Rg)

plt.xlim(c1[2], c1[3])
plt.xlabel("Volume (ml)")
plt.title("Expected chromatogram peak for your protein in corresponded volume")
plt.xlim(0, c1[3])
plt.xticks(np.arange(0, c1[3], step=(c1[3]/10)))
plt.bar(x, Rg_pro, width=Rg_pro/300)
#plt.show()
plt.savefig("peak_prediction.png")




f=open("peak_prediction_output.html",'w')
f.write("""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    """)
f.write("<head>\n")
f.write("<title></title>\n")
f.write("</head>  \n")
f.write("<body>\n")
f.write("Your column volume is %s ml, and you can purify protein between %s-%s kDa or %s-%s A (in case of radius of gyration, assuming the protein is globular)" % (c1[3], c1[4], c1[5], c1[0], c1[0]))

f.write('<p class="PeakPrediction"></p>\n')
f.write('<img src=peak_prediction.png />\n')


f.write("</body>\n")
f.write("</html>\n")
f.close()


print("I saved .png file and a .html file in your directory, have fun!")













