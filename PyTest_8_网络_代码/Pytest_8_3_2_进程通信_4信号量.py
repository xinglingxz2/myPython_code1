'''    实例 成功演示。 信号灯集
信号量： 进程间 标志性 数据，（一般用于进程数量判断, 新建进程-1）
方法： sem = Semaphore(num)  # 创建信号量对象，参数：初始值。必须写
      sem.acquire()  # 信号量减1  为0时阻塞
      sem.release()  # 信号量加1
      sem.get_value() # 获取信号量数值
线程间通信 注意点： 父进程中打开文件，子进程从父进程内存空间获取内容名，
        会有一定的影响，避免影响放在子进程中打开。

'''

# 1.导入
from multiprocessing import Semaphore,Process
from time import sleep
import os

# 2.创建信号量
sem = Semaphore(3)  # 服务程序最多允许3个进程同时执行。

def handle():
    print("%d  执行申请信号量？"%os.getpid())
    sem.acquire()  # 3.每次执行新进程 信号量-1
    print("%d  开始执行进程操作。。。" % os.getpid())

    print("-------------信号量值为",sem.get_value()) # 查询信号量
    sleep(2)
    print("%d  进程执行完毕" % os.getpid())
    sem.release()  # 4. 关闭进程  信号量+1

jobs =[]
for i in range(10):
    p = Process(target=handle)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()  # 注销进程
print("-------------信号量值为",sem.get_value())