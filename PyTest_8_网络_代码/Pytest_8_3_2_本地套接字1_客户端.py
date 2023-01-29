'''  进程通信: 使用文件套接字: 客户端：  实例 成功演示，
 应用：本地 应用软件间的 通信。 （不是网络间的通信）
 特点：无任何关系的进程间 通信。               127.0.0.1

 1.创建本地套接字  sockfd = socket(AF_UNIX, SOCK_STREAM)
 2.绑定本地套接字文件  sockfd.bind(file)

 3.监听，接收链接，消息收发  linten() -- accept() -- recv() ,send()
cookie:
   Linux文件：  b块设备    c字符
               d目录      -普通
               l链接      s套接字 （ ）
               p管道 （有名管道）

'''


# 1.导入
from socket import *
import os
from multiprocessing import Process  # 导入多进程
from random import randint  # 导入随机整数


# 2.确定 本地套接字文件
sock_file = "./sock"  # 本地文件夹下 创建套接字文件sock

if os.path.exists(sock_file ) :   # 判断文件是否存在
    os.remove(sock_file)    # 删除文件


# 3.创建本地套接字
sockfd = socket(AF_UNIX, SOCK_STREAM)

# 4.绑定本地套接字文件
sockfd.bind(sock_file)

# 5.监听， 链接
sockfd.listen(3)  #
while True:
    c, addr = sockfd.accept()  #
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
    c.close()
sockfd.close()