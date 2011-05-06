#!/usr/bin/python
# -*- coding: iso-8859-1 -*

def minimumScalar(u,v) :
	u.sort()
	v.sort()
	v.reverse()

	i=0
	for x, y in zip(u,v):
		i += x*y

	return i

def parseVector(s) :
	s_string = s.split()
	return [int(i) for i in s_string]

f = open('A-large-practice.in','r')
T = int(f.readline())
i = 1

while (i <= T):
	n = f.readline()
	u = parseVector(f.readline())
	v = parseVector(f.readline())
	r = minimumScalar(u,v) 
	print('Case #' + repr(i) +': '+ repr(r))
	i+=1

#u = [1,3,-5]
#v = [-2,4,1]

#a = [1, 2, 3, 4, 5]
#b = [1, 0, 1, 0, 1]

#print(minimumScalar(u,v))
#print(minimumScalar(a,b))









