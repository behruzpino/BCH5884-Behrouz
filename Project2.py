#!/usr/bin/env python3
#https://github.com/behruzpino/BCH5884-Behrouz.git
#Behrouz_Ghazi_Esfahani



import numpy
from matplotlib import pyplot
import peakutils
from peakutils.plot import plot as pplot


#first:FIle_opening
f=open("superose6_50.asc")
lines=f.readlines()
f.close()

t=[]
a=[]

#stripping the lines
for line in lines[3:]:
	words=line.split()
	try:
		t.append(float(words[0]))
		a.append(float(words[1]))
	except:
		print ("could not parse", line)
		continue


t=numpy.array(t)
a=numpy.array(a)


#getting the slope and slope's slope to identify the peaks
da=numpy.gradient(a)
dda=numpy.gradient(da)
#pyplot.plot(t,da)

#filling the area underneath the peaks
pyplot.fill_between(t, a, 32, where =abs(da) > 1.3, color='green')
pyplot.fill_between(t, a, 32, where =abs(dda) > 0.8, color='green')


#Using peakutils to find the local maximums, we can change the threshold based on our data
indexes = peakutils.indexes(a, thres=.05, min_dist=31)
#print(indexes)
for i in range(len(indexes)):
	print("You have one peak at the time=", t[indexes][i], "with the absorption of", a[indexes][i], "mAU")
#pyplot.figure(figsize=(8,4))
pplot(t, a, indexes)
pyplot.plot(t,a)


pyplot.show()
