'''   重点代码   测试成功  tcp服务端:
   并发： 时间切片轮循多程序同时运行。（同时运行）
网络并发通信1： 基于fork的多进程网络并发模型。


'''

from socket import *
import os,sys
import signal  # 僵尸进程处理  3信号处理

#---------------------------------------------------------------------
# 子进程客户端处理函数
def newProcessFun(c):
    print("客户端：",c.getpeername())
    while True:
        data = c.recv(1024)  # 添加异常判断
        if not data:
            break
        print(data.decode()) # 接收完数据 打印显示。 ---具体可以在此处理数据----
        c.send(b"OK_A1")  # 发出登录成功信息        ---具体可以在此处理数据----
    c.close()


#---------------------------------------------------------------------
# 创建监听套接字
HOST = '0.0.0.0'  # IP地址  '0.0.0.0'
PORT = 8888  # 端口号
ADDR = (HOST,PORT) #网络地址

s = socket()  # 创建TCP套接字
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) # 设置端口的立即重用
s.bind(ADDR)   # 绑定
s.listen(3)  # 监听

# 僵尸进程处理
signal.signal(signal.SIGCHLD,signal.SIG_IGN)   # signal.SIGCHLD

print("Listen the port 8888 ...")

# 循环等待客户端链接
while True:
    try:
        c,addr = s.accept()  # 等待接收客户端的请求
    except KeyboardInterrupt:  # ctrl +C 异常退出
        sys.exit("服务器退出")
    except Exception as e:   # 其他异常
        print(e)
        continue

    # 创建子进程处理客户端请求
    pid = os.fork()  # fork创建子进程
    if pid == 0:  # <0 创建子进程错误， ==0创建成功。
        s.close() # 子进程关闭不需要的s套接字。
        newProcessFun(c) # 具体处理客户端请求函数
        os._exit(0) # 退出子进程  # 设定退出状态值0

    # 父进程实际只用来处理客户端链接
    else:
        c.close() # 父进程关闭不需要的c链接套接字




