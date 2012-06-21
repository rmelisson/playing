from Parser import Parser
import itertools

"""
You decide to use your data to find the people most compatible with each other.
Two people are compatible if they have at least 2 bands in common. 
The compatibility of two people is directly pro- portional to the number of 
bands they like in common. For each person in the list, output the most 
compatible person(s). If there is more than one compatible person, separate 
the names with a comma. If a person has nobody compatible, output nothing.

Note :
- - - 
  Even if I didn't use a dedicated structure, it is a graph problem.
  Colleagues are vertices (labeled by name) and the number of bands 
  they like in common is the weight of edges.
  This is a complete graph because we can calculate the proximity 
  between every pair of colleagues (n*(n-1)/2 edges).
  Here I design an algorithm which select for each vertice the corresponding
  vertice(s) with the maximum weigthed edge(s).
"""
def core(nameA, nameB, i, results):
  """ replace or append a colleague in results depending on proximity i """
  if nameA not in results :
    results[nameA] = (i, [nameB])
  elif nameA in results :
    if results[nameA][0] < i :
      results[nameA] = (i, [nameB])
    elif results[nameA][0] == i : 
      results[nameA][1].append(nameB)

def problem4(filename):
  
  parser = Parser(filename)
  colleague_bands = {}
  names = set()

  while True :
    try :
      current_line = parser.next()
    except StopIteration:
      break
    name = current_line[0]
    names.add(name)
    bands = current_line[1]
    colleague_bands[name] = set()
    for band in bands :
      colleague_bands[name].add(band)

  # we create all the possible combinations beween colleagues
  # WARNING : this is potientially costly to compute -> n*(n-1)/2 edges
  pairs = itertools.combinations(names, 2)
  
  # results : {'Bob': [2, ['Alice']], 'Alice': [5, ['Mike', 'John']]...}
  # means Alice likes 5 bands in common with Mike and John
  results = {}
  for (name1, name2) in pairs :
    # bands that both like
    both = colleague_bands[name1] & colleague_bands[name2]
    i = len(both)
    # at least 2 bands in common
    if i>1:
      core(name1, name2, i, results)
      core(name2, name1, i, results)

  # print results
  for name in names:
    s = ""
    if name in results :
      (i, l) = results[name]
      s = ", ".join(l)
    print name + ": " + s

#problem4("dataset")
problem4(None)
