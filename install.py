import socket

domain = input ("Type Website Link: ")
ip = socket.gethostbyname(domain)
ip2 = "Ip Is:"
ip3 = "Enjoy:)"
print (ip2+ip)
print (ip3) 
