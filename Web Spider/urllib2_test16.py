import urllib2  
try:  
    response = urllib2.urlopen('http://bbs.csdn.net/why')  
except urllib2.HTTPError, e:  
    print e.code  
