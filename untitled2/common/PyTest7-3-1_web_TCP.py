'''
TCP/数据流 服务器 接收代码
'''

#import socket
from socket import *

m=0
sockfd = socket.socket()   # 1. 创建套接字

#设置套接字端口异常后立即重用
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)

sockfd.bind( ( '192.168.1.14' , 8888) )    # 2. 绑定本机
sockfd.listen(5)   # 3 设置监听
while True:
    print("等待客户端连接...")
    try:
        connfd, addr = sockfd.accept()  # 4 等待连接
        print("客户端地址： ",addr)
    except KeyboardInterrupt:
        print("退出服务")
        break
    while True:
        data = connfd.recv(1024)   # 5 接收数据
        if not data:
            break
        print("收到的消息是：  " ,data.decode())

        m = m+1
        strA =  "您好客户端，已经收到您的消息,这是第" + str(m) + "次回复"
        n = connfd.send( strA.encode() )  #  发送数据
        print( "发送了%d字节数据"%n)
    connfd.close()     # 6 关闭客户端

sockfd.close()  # 关闭连接


#///////////////////

# sockfd = socket()
#
# server_add = ('192.168.1.14',8888)
# sockfd.connect(server_add)
#
# sockfd.send("来自客户的消息".encode())
# data = sockfd.recv(1024)
# print ("来自服务器：",data)
#
# sockfd.close()