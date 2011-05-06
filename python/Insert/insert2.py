#Recoller les morceaux 'Saint, Maurice' -> 'Saint Maurice'
def reformat(l):
	l_ret = []
	ok = True
	for e in l:
		if not ok:
			tmp += ' ' + e
			if e.endswith("'"):
				l_ret.append(tmp)
				ok=True
		elif (e.startswith("'")) and (not e.endswith("'")):
			ok = False
			tmp = e
		else:
			l_ret.append(e)
	return l_ret

import string
print "bonjour!"
s = "'blabl' 2 'cool man'"
l = string.split(s)
s3 = reformat(l)
print s
print l
print s3
