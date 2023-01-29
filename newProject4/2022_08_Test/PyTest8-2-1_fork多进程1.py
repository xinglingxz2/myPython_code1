''' Python 8-2-1  多并发   windows系统 不能正常使用   multiprocessing模块就是跨平台版本的多进程模块
  #  fork(): 创建新进程，  os.getpid():获取本进程的pid值   os.getppid():获取父进程的pid值
        os._exit(1): 结束进程     sys.exit("提示语") ：结束进程
'''

#coding=utf-8
import os
from time import sleep
import sys

pid = os.fork()

if pid < 0:
    print("build new process is failed失败...")
elif pid == 0:
    print("成功创建新个子进程:",os.getpid())
    print("本子进程的父进程是= ",os.getppid())
    os._exit(2)  #  子进程退出 返回 2 * 256   == 512
else:
    print("我是父进程，my pid is %d"%(os.getpid), "我的孩子是",pid)
    # pid,status = os.wait()  # 等待处理僵尸进程  阻塞等待
    pid,status = os.waitpid(-1,os.WNOHANG)  # 非阻塞  可用循环x秒 反复执行
    print("结束的子进程pid",pid)
    print("status: ",status )   #显示原值2：可以 /256   (或os.WEXITSTATUS(status)   )