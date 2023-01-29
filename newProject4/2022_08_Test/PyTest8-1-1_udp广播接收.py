'''  broadcast_recv.py
    广播接收
'''

from socket import *

s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)  # 让套接字可以接收广播
s.bind(('0.0.0.0',9999))  #

while True:
    try:
        msg,addr = s.recvform(1024)
    except KeyboardInterrupt:
        break
    else:
        print(msg.decode())



