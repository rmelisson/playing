from Parser import Parser
"""
You want to determine band following. Write a program to output the band name
followed by the colleagues who like the band.
"""
def problem2(filename):

  parser = Parser(filename)
  bands_colleagues = {}
  
  while True :
    try :
      current_line = parser.next()
    except StopIteration :
      break
    colleague_name = current_line[0]
    bands = current_line[1]

    for band in bands :
      if band in bands_colleagues :
        bands_colleagues[band].append(colleague_name)
      else :
        bands_colleagues[band] = [colleague_name]

  for (band, names) in bands_colleagues.items():
    print band + ': ' + ', '.join(names)

#problem2("dataset")
problem2(None)
