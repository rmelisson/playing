import sys

class Parser:
  """ A parser class which can read stdin or into a file """

  def __init__(self, filename):
    if filename :
      self.f = open(filename, 'r')
      self.n = int(self.f.readline())
    else :
      self.f = None
      self.n = input()
    if self.n in [0, 1]:
      print "Hmmm... " + repr(self.n) + " person is not a team."
      sys.exit(0)
   
  def next(self):
    if (self.n > 0):
      if self.f :
        line = self.f.readline()[:-1]
      else:
        line = raw_input()[:-1]
      line_cut = line.partition(": ")
      # colleague name
      colleague = line_cut[0]
      # bands this colleague likes
      bands = line_cut[2].split(', ')
      self.n -= 1
      return (colleague, bands)
    else:
      raise StopIteration
