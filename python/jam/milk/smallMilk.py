#!/usr/bin/python
# -*- coding: iso-8859-1 -*

# C : number of test case
# N : number of milshake flavour
# M : number of customer
# T : number of milkshakes a customer like
# 0 unmalted, 1 malted

class Result:
	def __init__(self, n):
		self.n = n
		self.t = []
		for i in range(0,n) :
			self.t.append(0)
		self.x = 0
			
#	def gimeMeNextShot():
#		if self.t == [] :
#			for i in range(0,n):
#				self.t.append(0)
#		return self.t


	def inc2(self):
		t = self.t
		# number of 1
		x = self.x
	
		i = 0

		if (x==self.n):
			self.t = []

		#  we locate where is the first 1
		while i < (self.n - self.x) :
			if t[i] == 1 : 
				if (i == (self.n - 1 - x)):
					self.x+=1
					t[0] = 1
					return	
				else : 
					t[i] = 0
					t[i+1] = 1
					return
			else :
				i+=1
		t[0] = 1
		return		



	def inc(self) : 
		i = 0
		while i < self.n :
			if self.t[i] == 0 :
				self.t[i] = 1
				return
			else :
				self.t[i]=0
				i+=1
		self.t = [] 
		
class CustomerTaste:
	
	def __str__(self) : 
		r = (repr(len(self.ts)) + ' :\n')
		for t in self.ts : 
			r+= t.__str__()
		return r

	def __init__(self, ts):
		self.ts = ts
		self.order()
		#self.t = len(ts)

	def order(self):
		new_ts= []
		for t in self.ts :
			if t.y == 0 :
				new_ts.insert(0,t)
			else :
				new_ts.append(t)
		self.ts = new_ts

	def check(self, shot):
		r = []
		for t in self.ts:
			if (shot[t.x-1] == t.y):
				# ok for this taste 
				r.append(t)
		#return the different available solution for this client taste
		return r

	def check2(self, shot):
		for t in self.ts:
			if (shot[t.x-1] == t.y):
				return True
		return False

	def getMaltedOne(self):
		for t in self.ts : 
			if t.y :
				return t.x
		return -1

class Taste:

	def __str__(self):
		return 'Taste -> x: ' + repr(self.x) + ' y: ' + repr(self.y)

	def __init__(self, x, y):
		self.x = x
		self.y = y

def testShotTogether(ll, shot) : 
	if len(ll) == 0 : 
		return True;

#	7l = ll[0]		

	for t in l :
		if (shot[t.x-1] < 20):
			shot[t.x-1] += 20
			b = testShotTogether(ll[1:],shot)
			if (b == False):
				shot[t.x-1] = t.y
			else: 
				return b

def selectBetter(rr):
	better = rr[0]
	i = sum(better)
	for r in rr[1:] :
		j = sum(r)
		if j < i :
			better = r
			i = j
	return better


def insertionSort(array):
    for j in range(1, len(array)):
        i = j - 1
        tmp = array[j]
        while i > -1 and (len(array[i].ts) > len(tmp.ts)):
            array[i+1] = array[i]
            i -= 1
        array[i+1] = tmp

def createListToSort(fromL) :
	newL = []
	for i in range(0,len(fromL)):
		newL.append([i,sum(fromL[i])])
	return newL

def sortIt(ll) :
	newL = createListToSort(ll)
	insertionSort(newL)
	returnL = []
	for i in newL :
		returnL.append(ll[i[0]])


def tryAShot(shot, c):
	ll = []
	# we assert that it is a valid shot for every client independantly
	for ct in c :
#		print(ct)
		l = ct.check(shot)
		if (l == []):
			return False
		else : ll.append(l)
	return True

	# if it is, we assert that it is valid for the clients together
#	for l in ll:
#		for t in l :
#			print(t)
#	return testShotTogether(ll, shot)

def cleanup(shot) :
	for i in range(0,len(shot)) :
		if shot[i]>=20 :
			shot[i] = shot[i] - 20
		 

def toString(r) :
	return " ".join(repr(i) for i in r)


# chained list of clients (sorted by boring first ?)
def findSolution(clients, i, result):

#	print repr(i) + ' result : ' + repr(result)
#	print(' i --> ' + repr(i))
	if i == len(clients) :
		return result

	if clients[i].check2(result) :
		return findSolution(clients, i+1, result)
	else :
		for t in clients[i].ts :
			if result[t.x-1] == 2 :
				new_result = result[:]
				new_result[t.x-1] = t.y
				new_new_result = findSolution(clients, i+1, new_result) 
				if new_new_result :
					return 	new_new_result
		return []


def algo(clients, result):
	r = result[:]
	while True :
		for client in clients :
			if client.check2(r) :
				print("continue")
				continue	
			else :
				i = client.getMaltedOne()
				if i>0 :
					r[i-1] = 1
					continue
				else : 
					return []
		return result
				



def clean2(result):
	for i in range(0,len(result)) :
		if result[i] == 2 :
			result[i] = 0 

def sortClients(clients):
	new_clients = insertionSort(clients) 

f = open('example.in', 'r')
#f = open('B-small-practice.in', 'r')
#f = open('B-large-practice.in', 'r')
C = int(f.readline())
i = 1

while (i <= C):
	n = int(f.readline())
	m = int(f.readline())
	c = []
	for j in range(0,m) :
		# we create the customer taste
		l = [int(j) for j in f.readline().split()]
		t = l[0]
		#print('t : ' + repr(t))
		l = l[1:]
		ts = []
		k = 0
		while k<len(l) :
			x = l[k]
			y = l[k+1]
			k+=2
			ta = Taste(x,y)
			ts.append(ta)
		c.append(CustomerTaste(ts))

#	print ' len c : ' + repr(len(c))
#	print ' n : ' + repr(n)
#	print ' m : ' + repr(m)
	sortClients(c)

	r = Result(n)

# 	result = findSolution(c,0,r.t)
	result = algo(c,r.t)
	clean2(result)
#	print toto
#	exit(0)

#	result = []
#	while (r.t):
#		shot = r.t[:]
#		if tryAShot(shot,c) == True:
#			result = shot
#			break
#		r.inc2()


#	rr = []
#	while (r.t):
#		rr.append(r.t[:])
#		r.inc()
#	sortIt(rr)
#
#	result = []
#	for shot in rr :
#		if tryAShot(shot,c) == True:
#			result = shot
#			break 
	
	
	p = 'Case #' + repr(i) +': '
	

#	iexit(0)
#	rr = []

#	while (r.t):
#		shot = r.t[:]
#		if tryAShot(shot,c) == True:
#			cleanup(shot)
#			rr.append(shot)
#		r.inc()


	if (result == []):
		p += 'IMPOSSIBLE'
	else :
		p += toString(result)

	print p
	i+=1

#	for cc in c:
#		for t in cc.ts:
#			print(repr(t.x) +','+ repr(t.y))
	# we should order c by t

	# r is the result, initialize by empty values (2)
#	r = []
#	for i : range(0,n) :
#		r = r.append(2)

#	r = resolve(c,r,0)
#	print('Case #' + repr(i) +': ' + r)
#	i+=1
