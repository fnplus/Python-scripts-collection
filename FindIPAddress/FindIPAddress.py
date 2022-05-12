import socket    

HostName = socket.gethostname()    
IPAddr = socket.gethostbyname(HostName)   

print(f"Your Computer Name is: {HostName}\n")    
print(f"Your Computer IP Address is: {IPAddr}")