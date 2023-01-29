'''  进程通信:  使用文件套接字: 服务端：  实例 成功演示，
  应用： 本地 应用软件间的 通信。 （不是网络间的通信）
      套接字 必须使用 字节串 格式
 1.创建本地套接字  sockfd = socket(AF_UNIX, SOCK_STREAM)
 2.绑定本地套接字文件  sockfd.bind(file)
 3.监听，接收链接，消息收发  linten() -- accept() -- recv() ,send()

'''


# 1.导入
from socket import *
import os

# 2.确定 本地套接字文件  相同
sock_file = "./sock"  # 本地文件夹下 创建套接字文件sock


# 3.创建本地套接字
sockfd = socket(AF_UNIX, SOCK_STREAM)
sockfd.connect(sock_file)

while True:
    msg = input("input >> ")
    if not msg:
        break
    sockfd.send(msg.encode())

sockfd.close()

