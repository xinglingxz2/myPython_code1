'''   实例 成功演示。
练习：进入聊天室，输入姓名，有提示进入名单，向某人发送消息，退出通知，群发消息
#  ------  客户端  client ----------

 客户端：  *

#--------------------------------------------------------------
# 协议   收到“OK_A1” 进入聊天室；  收到“Error_BB” 程序正在退出
#       请求类别：  L  进入请;  C  聊天信息;  Q  退出聊天室

退出聊天室：
    客户端：  输入quit或者   ctrl+c 异常退出
             将退出请求发送给 服务端
             结束进程
             接收进程 收到EXIT 退出进程
    服务端：  接收客户的退出消息
             将退出消息告知其他人
             给退出用户发送EXIT
             删除该用户在 用户登录字典 的内容

'''

import os, sys
from socket import *
from time import sleep

#--------------------------------------------------------------
#  服务器地址
Addr = ("192.168.1.10", 8888)


def send_msg(s,name) :  # 发消息 函数  多进程
    while True:
        try:
            text = input("发言信息： ")
        except KeyboardInterrupt:  # 异常退出处理
            text = "quit"
        if text == "quit":  #  ---退出聊天室 -----
            msg = "Q " + name
            s.sendto(msg.encode(), Addr)
            sys.exit("---退出聊天室 ----")
        msg = "C %s %s"%(name,text)  # 消息格式： C_接收用户名_发送的消息
        s.sendto(msg.encode(),Addr)

def recv_msg(s):   # 收消息 多进程( 1接收信息， 2退出）
    while True:
        data,addr = s.recvfrom(2048)
        # 服务端发送 EXIT 让客户端 退出
        if data.decode() == "EXIT":
            sys.exit()
        print(data.decode()+ "\n发言：",end='')  # 打印完 重新开一行
#--------------------------------------------------------------
# 发出请求
def faSong(s):
    while True:
        name = input(" 请输入姓名 ...") #
        msg = "L "+ name
        s.sendto(msg.encode(),Addr)

        # 等待回应
        data,addr = s.recvfrom(1024)  #
        if data.decode() == "OK_A1":
            print("-----您已经进入聊天室-----")
            break
        elif data.decode() == "Error_BB":
            print("+++  程序正在退出 +++")
            pass
        else:
            print(data.decode())  # 打印服务器返回信息

        # ---------   创建多进程   -------------

        recv_msg(s)   # 收消息
        send_msg




# ===============================================================
# 1. 创建网链接
def main():
    # 套接字
    s = socket(AF_INET, SOCK_DGRAM)  # 创建套接字UDP

    # 登录聊天室
    faSong(s)  # 处理客户端请求  参数：套接字处理收发


if __name__ == "__main__":
    main()





