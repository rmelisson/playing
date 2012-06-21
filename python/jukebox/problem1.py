from Parser import Parser

"""
Write a program to find the top 2 liked bands. If there is a tie, output all 
the matching bands. Each band should be on a new line. The output order is 
unimportant. 
"""
def problem1(filename):

  # dictionary storing occurence of bands
  bands_count = {}

  parser = Parser(filename)
  while True :
    try :
      current_line = parser.next()
    except StopIteration :
      break
    bands = current_line[1]
    # if the band has already been discovered, we increment the number 
    # of occurence if not, we insert it with 1 
    for band in bands:
      if band in bands_count :
        bands_count[band] += 1
      else :
        bands_count[band] = 1

  # n and m represent the first and second bigger occurences of bands
  # several bands can be stored into it because of ties, so we store the 
  # number of occurence and the list of bands
  n = [0]
  m = [0]
  for (b, i) in bands_count.items():
    # if we find a bigger count, we move n to m and create the new n
    if i > n[0] :
      m = n
      bands = [b]
      n = [i, bands]
    # if the count is the same than n (or m), we add the band to n (or m) list
    elif i == n[0]:
      n[1].append(b)
    elif i == m[0]:
      m[1].append(b)
    # if we find a count smaller than n but bigger than m we update the second
    elif i>m[0] :
      bands = [b]
      m = [i, bands]

  # then we print the names
  for name in n[1]:
    print name
  for name in m[1]:
    print name

#problem1("dataset")
problem1(None)
