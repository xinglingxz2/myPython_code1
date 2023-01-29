'''
# #  聊天室 --  ----  服务器端 ----
'''



from socket import  *
import  os, sys

ADDR = ("192.168.1.15",8888)  # 服务器地址
userLogin = {}  # 已经登陆的用户 字典信息

def do_login(s,name,addr):
    if name in userLogin:
        s.sendto("该用户已经被使用，请重新输入用户名...".encode(),addr)
        return
    else :
        s.sendto(b"OK_A1",addr)
        # 通知其它人，
        msg = "欢迎%s进入聊天室 :) "%(name)
        for i in userLogin:
            s.sendto(msg.encode(),userLogin[i])  # 每个用户的地址 为字典的值  i为用户字典的键
        userLogin[name] = addr # 将使用用户加入到字典

#请求处理  -- 来自客户端的登陆
def  do_request(s):
    while True:
        data,addr = s.recvfrom(1024)  # 接收信息
        print(data)
        msg = data.decode().split(' ') # 使用空格 分割字符串 为列表
        if msg[0] == "L":
            name = msg[1]  # 读取的为 用户名
            do_login(s,name,addr) #
        elif msg[0] == "C":
            info = msg[1]  # 读取的为信息

#============================================================
def main():
    s = socket(AF_INET,SOCK_DGRAM)  # 创建套接字
    s.bind(ADDR)   # 绑定地址

    do_request(s) # 处理客户端请求

if __name__ == "__main__":
    main()