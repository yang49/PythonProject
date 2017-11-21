import netifaces

print("Hi");

print (netifaces.interfaces());

for x in netifaces.interfaces():
	addr = netifaces.ifaddresses(x);
	print(addr);
	print("");