__author__ = 'Ben'
import pickle, urllib

#file = open("peakhell.txt")
#o = file.read()
o = pickle.load(urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))
print(o)