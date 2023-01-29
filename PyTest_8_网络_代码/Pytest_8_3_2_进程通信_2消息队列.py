'''  消息队列:  单向进出，先进先出，队列排序。   实例 成功演示
方法：  .put(data,[block,timeout]) 参1：向队列存入的数据。 参2：是否阻塞，False为非阻塞。参3：超时检测
       .get([block,timeout]) 从队列读取消息。 可选参数同上
       .full() 判断列队是否为满
       .empty() 判断列队是否为空      别太快
       .qsize() 获取列队中的消息个数
       .close() 关闭列队

'''

# 1.导入
from multiprocessing import Queue    # 导入队列
from multiprocessing import Process  # 导入多进程
from time import sleep
from random import randint  # 导入随机整数


q = Queue(9) # 2.创建对象  参数：队列最多存放的消息个数(必须写)。  返回消息对象

def request():
    for i in range(20):
        x = randint(0,100)  # 随机整数 0-100以内
        y = randint(0,100)
        q.put((x,y))  # 3.队列导入数据（可以是任何类型）

def handle():
    while True:
        #sleep(0.5)
        try:
            x,y = q.get(timeout= 3)  # 4. 从队列读取消息, 超时延时3秒
        except:
            break
        else:
            print("%d + %d = %d"%(x,y,x+y))

p1 = Process(target= request)  # 进程1 指定函数
p2 = Process(target= handle)   # 进程2 指定函数


p1.start()   # 启动进程
p2.start()

p1.join()  # 回收进程
p2.join()
