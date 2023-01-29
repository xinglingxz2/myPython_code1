'''
UDP/数据报 服务器 接收代码
'''

import socket
# from socket import *


sockfd = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   # 1. 创建套接字
sockfd.bind( ( '192.168.1.2' , 8888) )    # 2. 绑定本机
while True:
    data,addr = sockfd.recvfrom(1024)  #  3. 收消息
    print("收到的消息是：",data.decode())
    print("  对方地址是： ",addr)
    sockfd.sendto("谢谢你的的连接".encode(),addr) # 4. 发消息
sockfd.close()