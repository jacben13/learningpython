__author__ = 'Ben'
import pickle

handle = open("peakhell.p","rb")
o = pickle.load(handle)
handle.close()
print(o)
# on page http://www.pythonchallenge.com/pc/def/channel.html
