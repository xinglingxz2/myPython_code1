'''
# 僵尸进程的处理 1  :
 pid,status = os.wait()     #  阻塞处理僵尸进程

 p s -aux  查看 进程树  :     kill -l  查看 系统信号
'''




def child_doing(cpid):
    print("this is child process",cpid)




import os
from time import sleep

pid = os.fork()   # 创建多进程
if pid < 0:
    print("Error")
elif pid ==0 :
    cpid = os.getpid()
    child_doing(cpid)
    os._exit(3)  # 设定退出状态值
else:
    # pid,status = os.wait()     #  阻塞处理僵尸进程  正常状态返回值为 0
    while True:
        sleep(0.0001)
        pid,status = os.waitpid(-1,os.WNOHANG)  # 等待僵尸处理  参数1： -1 任意子进程      参数2：  0 阻塞等待，  WNOHANG 非阻塞
        print("pid: ",pid)
        print("status: ",status//256)   # 获取子进程的退出是什么引起的   整除256


