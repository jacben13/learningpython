__author__ = 'Ben'
import urllib.request
import re

n = 8022
s = ""
p = re.compile("\\d+")
prefix = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
while s == "":
    f = urllib.request.urlopen(prefix+str(n)).read()
    print("going to : " + prefix + str(n))
    print(f)
    n = p.findall(str(f))
    print("matched :%s" % n)
    n = n[len(n)-1]
    print(n)
    #s = input("continue?")