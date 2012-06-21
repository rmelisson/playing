from Parser import Parser

"""
Your colleagues are happy if they can listen to their liked band at least once
a day. Assuming,
  1. Each song lasts for 5 mins.
  2. You have only 1 song from each band in your playlist. 
  3. A work day lasts 8 hours.
Write a program to maximize the number of happy people in your office. 
If there are multiple cor- rect outputs, output any one. 
Your output should be a list of artists separated by a new line (order 
unimportant). 



Note : 
- - - 
  While we make a lot of comparison between list in this problem,
  we should probably use something more efficient than Python sets
  for retrieving the size of lists intersection (see * below).
  For example we may represent list of names by a vector of bits.
  By doing this, it could be really inexpensive to get the numbers of names 
  which are present in both lists we compare.
"""
def find_closer_band(bands_colleagues, unhappy):
  # (name, occurences)
  best = ("", 0)
  for (band, colleagues) in bands_colleagues.items():
    """ *here """
    intersection = unhappy & colleagues
    i = len(intersection)
    if i > best[1] :
      best = (band, i)
  return best[0]

def problem3(filename):
  parser = Parser(filename)

  # associate one band to all colleagues who like it
  # {'The Doors' : ['Alice', 'Bob'], 'U2' : ['Bob'], ... }
  bands_colleagues = {}

  # set of colleagues who are not satisfied yet
  unhappy_colleagues = set()

  while True :
    try :
      current_line = parser.next();
    except StopIteration :
      break
    name = current_line[0]
    bands = current_line[1]
    for band in bands :
      if band in bands_colleagues:
        bands_colleagues[band].add(name)
      else :
        bands_colleagues[band] = set()
        bands_colleagues[band].add(name)
    unhappy_colleagues.add(name)

  """
  While there is still unhappy colleagues :
    find the band who is the most liked by remaining unhappy colleagues
    add this band to the result
    remove colleague who like this band from the unhappy list
  """
  result = []
  while unhappy_colleagues :
    band = find_closer_band(bands_colleagues, unhappy_colleagues)
    result.append(band)
    for colleague in bands_colleagues[band]:
      if colleague in unhappy_colleagues :
        unhappy_colleagues.remove(colleague)

  for band in result :
    print band

#problem3("dataset")
problem3(None)
