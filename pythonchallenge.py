__author__ = 'Ben'
import pickle

handle = open("peakhell.p","rb")
o = pickle.load(handle)
handle.close()
print(o)