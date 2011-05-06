#!/usr/bin/python
# -*- coding: iso-8859-1 -*

#f = open('example.in')
f = open('B-large-practice.in')

N = int(f.readline())
count = 0
while count < N :
	l = f.readline()
	ll = l.split()
	ll.reverse()
	p = " ".join(ll)
	print 'Case #' + repr(count+1) + ': ' + p
	count += 1

