import urllib2  
my_url = 'http://www.google.cn'  
response = urllib2.urlopen(my_url)  
redirected = response.geturl() == my_url  
print redirected
print response.geturl()
  
my_url = 'http://rrurl.cn/b1UZuP'  
response = urllib2.urlopen(my_url)  
redirected = response.geturl() == my_url  
print redirected
print response.geturl()
