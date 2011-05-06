#!/usr/bin/python
# -*- coding: iso-8859-1 -*


#f = open('example.in')
f = open('A-large-practice.in')
N = int(f.readline())
count = 0
while count < N :
	C = int(f.readline())
	l = int(f.readline())
	L = [int(p) for p in (f.readline()).split()]
	
	LL = [[L[i],i] for i in range(l)]

	LL.sort()
	LL.reverse()
	NL = []
	for e in LL :
		if e[0] < C :
			NL.append(e)

#	print C
#	print NL
	result = 0

	for i in range(len(NL)-1) :
		for j in range(i+1,len(NL)) :
			r = NL[i][0] + NL[j][0]
			if (r > C):
				continue
			elif (r > result):
				result = r
				x = NL[i][1]
				y = NL[j][1]
				break
	
	p = "Case #" + repr(count + 1) + ": "
	if (x<y):
		p+= repr(x+1) + ' ' + repr(y+1)
	else : 
		p+= repr(y+1) + ' ' + repr(x+1)
		
	print p		

	count+=1
exit(0)


#	L.sort()
#	L.reverse()
#	result = 0

#	for i in range(0,l-1) :
#		if L[i] > C : 
#		for j in range(i+1,l) :
#			r = L[i] + L[j]
#			if r > C :
#				# we should inc i
#			else : 
#				if r > result :
 #					# we should inc j
#				else : 
#					# we should inc i	
#					pass;
#	print C
#	print L
#	N-=1
	

