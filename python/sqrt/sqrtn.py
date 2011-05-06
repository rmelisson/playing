#!/usr/bin/python
# -*- coding: iso-8859-1 -*
from math import *

def newton(n):
	sum = 0
	factn = factorial(n)
	for i in range(1,n+1) :
		f = 1
		if n%2 == 0 :
			powsqrt = pow(5, (n-i)/2)
		else :
			powsqrt = pow(5, (n-i-1)/2)
			f = sqrt(5)
			
		sum += (factn * pow(3,i) * powsqrt * f) / ((factorial(i) * factorial(n-i)))
	return sum 

print newton(5)
	
