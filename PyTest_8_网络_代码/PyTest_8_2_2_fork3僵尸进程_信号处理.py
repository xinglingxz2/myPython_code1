'''
# 僵尸进程的处理 3 :  通过信号处理
   使用signal模块在父进程创建子进程前写下   语句：
   import signal
   signal.signal(signal.SIGCHLD,signal.SIG_IGN)
   特点： 非阻塞 处理所有子进程
'''


import os
import signal
from time import sleep

# 处理子进程退出, 使用信号处理
signal.signal(signal.SIGCHLD,signal.SIG_IGN)


def f0_doing():   # 父类进程
    for i in range(5):
        sleep(2)
        print("parent 进程 test code...000000000")


def f1_doing():   # 二级子进程
    for i in range(5):
        sleep(1)
        print("一级子进程 test code...1111111111")




pid = os.fork()  # 创建多进程
if pid < 0:
    print("Error")
elif pid == 0 :
    f1_doing()
else:
    f0_doing()