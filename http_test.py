import socket
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 5555))

# # Echo client program
# import socket
# 
# HOST = '127.0.0.1'    # The remote host
# PORT = 5555              # The same port as used by the server
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))
# s.send('Hello, world')
# data = s.recv(1024)
# s.close()
# print 'Received', repr(data)

#socket.connect('http://127.0.0.1/instrumentation/nd/range?value=10&submit=update', '5555')

