from socket import *
import time

serverName = '127.0.0.1'
serverPort = 12002
MESSAGE = 'ping'

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

for i in range(5):
	send_time = time.time()
	clientSocket.sendto(MESSAGE.encode(), (serverName, serverPort))
	print ('i=',i)

	try:	
		modifiedMessage, serverAdress = clientSocket.recvfrom(2048)
		recv_time = time.time()
		rtt = recv_time - send_time	
					
		print('Ping. Round Trip Time', rtt)
	except:
		print("Request timed out")

clientSocket.close()
