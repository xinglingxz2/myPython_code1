'''
# 僵尸进程的处理 2 :   利用二级子进程变为孤儿进程,处理僵尸进程，一级子进程主动退出，使二级子进程成为孤儿进程。
'''


import os
from time import sleep


def f0_doing():   # 父类进程
    for i in range(5):
        sleep(2)
        print("parent 进程 test code...000000000")


def f2_doing():   # 二级子进程
    for i in range(5):
        sleep(1)
        print("二级子进程 test code...222222222")




pid = os.fork()  # 创建多进程
if pid < 0:
    print("Error")
elif pid == 0 :
    p = os.fork()   # 二级子进程
    if p == 0:
        f2_doing()   # 二级子进程执行体
    else:
        os._exit(0)  # 一级子进程设定退出状态值
else:
    pid,status = os.wait()     #  阻塞处理僵尸进程  正常状态返回值为 0
    f0_doing()

    '''

    '''

