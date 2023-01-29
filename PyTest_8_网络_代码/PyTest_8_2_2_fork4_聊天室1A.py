'''  实例 成功演示。
练习：进入聊天室，输入姓名，有提示进入名单，向某人发送消息，退出通知，群发消息
#  ------  服务端   server ----------

#--------------------------------------------------------------
# 协议   发出“OK_A1” 进入聊天室；  发出“Error_BB” 不允许进入聊天室
#       请求类别：  L  进入请;  C  聊天信息;  Q  退出聊天室

  “”“
        try :  #  ====？？？？？？=====
            userLogin[name] = addr
        except:  # 使用异常调试  查看 信息 正确？？
            print("userLogin[%s] = %s"%(name,userLogin[name]))
            ”“”


'''

import  os,sys
from socket import *
from time import sleep
#--------------------------------------------------------------
#  服务器地址
Addr = ("192.168.1.10",8888)

userLogin = {}   # 正在使用的用户   登录信息字典
#--------------------------------------------------------------

# 多线程  --本段未使用--
def duoXianCheng(s):
    pid = os.fork()  # 创建多进程
    if pid < 0:
        print("Error")
    elif pid == 0:

        os._exit(3)  # 设定退出状态值
    else:
        while True:
            pid, status = os.waitpid(-1, os.WNOHANG)  # 等待僵尸处理  参数1： -1 任意子进程      参数2：  0 阻塞等待，  WNOHANG 非阻塞
            do_request(s)
# --------------------------------------------------------------
# 打开文件
# fd = open("liaoTianUser.txt","r+")  # 字符串形式保存

# --------------------------------------------------------------
# 登录系统
# 存储结构  使用：字典  {name:addr , ...}
def do_login(s,name,addr):    # s:其他人   msg[1]: 姓名   addr:网址ip
    if name in userLogin:
        s.sendto("该用户名已经被使用，请重新输入用户名...".encode(),addr)
        return
    else:
        s.sendto(b"OK_A1",addr)
        # 通知其他人，有用户登录了
        msg = "欢迎%s进入聊天室 ：）"%(name)
        for i in userLogin:
            s.sendto(msg.encode(),userLogin[i])  # 地址为用户字典的值
        # 将使用用户加入 字典
        userLogin[name] = addr



def do_chat(s,name,info):  # 聊天函数 群发  !(把信息转发给指定用户)
    msg = "\n %s : %s"%(name,info)
    for i in userLogin:
        if i != name:   #
            s.sendto(msg.encode(),userLogin[i])

def do_quit(s,name,addr):  # 让客户退出聊天室
    msg1 = "%s退出了聊天室 "%name
    msg = "Error_BB"
    if name not in userLogin:  #
        s.sendto(msg.encode(),addr)
    else:
        s.sendto(msg.encode(), userLogin[name])
    for i in userLogin:  # 给群内客户发xx退出通知
        if i != name:
            s.sendto(msg1.encode(),userLogin[i])
    # 将退出用户在 用户登录字典中删除
    del userLogin[name]

# ---请求处理--接收客户端登录-----------------------------
def do_request(s):
    while True:
        data,addr = s.recvfrom(1024)  # 接收消息
        data = data.decode()   #
        print(data)   # *** 可删 ***
        msg = data.split(' ')  # 使用空格分割字符串 为列表
        if msg[0] == 'L':
            name = msg[1] # 读取用户名
            do_login(s,name,addr)  # s:其他人   msg[1]: 姓名   addr:网址ip
        elif msg[0] == 'C':
            name = msg[1] # 读取用户名
            info = ' '.join(msg[2:])# 读取信息  *** 列表拼接 （使用' '空格符 链接）
            do_chat(s,name,info)  # # 聊天函数  把信息转发给指定用户
        elif msg[0] == 'Q':
            name = msg[1] # 读取用户名
            do_quit(s,name,addr)  #

# 子进程 管理员发送群消息
def childProcessforUser(s):
    msg = input("管理员消息：")
    msg = "C 管理员消息 "+ msg
    s.sendto(msg.encode(),Addr)

# ===============================================================
#  1. 创建网链接
def main():
    # 套接字
    s = socket(AF_INET,SOCK_DGRAM)  # 创建套接字
    s.bind(Addr)   # 绑定地址

    # 多线程处理
    pid = os.fork()  # 创建多进程
    if pid < 0:
        print("Error")
    # 管理员 特殊处理信息
    elif pid == 0:
        # 通过子进程 把信息发给父进程，通过父进程转发给群用户
        childProcessforUser(s)
    #  主线程 处理网络常规信息
    else:
        do_request(s)  # 处理客户端请求  参数：套接字处理收发



if __name__ == "__main__":
    main()





