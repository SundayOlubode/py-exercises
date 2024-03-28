import socket
#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('data.pr4e.org',  80))
#cmd = ('GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n').encode()
#mysock.send(cmd)

#while True:
#    data = mysock.recv(500)
#    if len(data) < 1:
#        break
#    print(data.decode(), end='')
    
    
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('data.pr4e.org', 80))
sock.sendall(b'GET http://data.pr4e.org HTTP/1.0\r\n\r\n')
count = 0
picture = b''
while True:
    data = sock.recv(5120)
    if len(data) < 1: break
    #time.sleep(0.25)
    count += len(data)
    print(len(data), count)
    picture = picture + data
sock.close()
pos = picture.find(b'\r\n\r\n')
file = open('cover1.jpg', 'wb')
picture = picture[pos+4:]
file.write(picture)
file.close()