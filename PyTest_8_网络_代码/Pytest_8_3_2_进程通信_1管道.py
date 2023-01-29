'''   实例 成功演示
进程间通信1--管道:   单向 或 双向 。
方法： Pipe(): 创建管道出入对象
      .send(data): 管道写入数据
      .recv() : 管道读取数据
'''

from multiprocessing import Process,Pipe
import os,time

# 不能重复import 同一内容

# 1.创建管道    参数：Flase :单向（1,读; 2,写）  | True ：双向 （默认）
fd1,fd2 = Pipe()  # 管道的出入两端


def fun(name):
    time.sleep(2)
    # 2.向管道写入内容
    fd2.send({name:os.getpid()})  #  内容为键值对：键：name 值：获取的pid值

jobs = []
for i in range(5):
    p = Process(target = fun,args=(i,)) # 指定进程函数与参数
    jobs.append(p)  # 加入列表
    p.start()  # 启动进程

# 父进程从管道接收消息
for i in range(5):
    data = fd1.recv()  # 3. 从管道读取消息
    print(data)


for i in jobs:
    i.join()  #  #回收进程



