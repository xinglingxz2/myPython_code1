'''
#  聊天室 -- 客户端——————
'''

from socket import  *
import  os, sys

# 服务器地址
ADDR = ("192.168.1.15",8888)    # 服务器的地址

# 发送测试
def faSong(s):
    print("********")
    name = input("you name...")
    msg = "L "+ name
    s.sendto(msg.encode(),ADDR)
    while True:
        # 等待回应
        data,addr = s.recvfrom(1024)
        if data.decode() == "OK_A1":
            print("----您已经成功登陆聊天室----")
            break
        elif data.decode() == "Error_BB":
            print("+++ 程序正在退出 +++")
            pass
        else:
            print(data.decode())  # 打印出服务器返回信息

#============================================================
# 创建网络连接
def main():
    s = socket(AF_INET,SOCK_DGRAM)  # 创建套接字
    faSong(s)

if __name__ == "__main__":
    main()