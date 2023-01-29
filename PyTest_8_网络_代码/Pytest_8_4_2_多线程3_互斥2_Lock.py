''' 互斥2：（互相排斥，保证只有1个线程 使用共用数据， 保证数据不紊乱。）
  Lock 线程锁
  创建： lock = Lock()  # 创建锁对象
  方法： lock.acquire() # 上锁   如果已经上锁，再调用就会阻塞等待（各个线程都设置，才能保证互斥）
        lock.release() # 解锁
  上锁方式2：  with  lock:  # 上锁
               ...       # with代码块结束自动解锁
'''

from threading import Thread, Lock

lock = Lock()  # 1.创建线程锁
a=b=0

def value():
    while True:
        lock.acquire()  # 上锁
        if a != b:
            print("a = %d, b = %d"%(a,b))
        else:
            print("a == b")
        lock.release()  # 解锁

t = Thread(target=value)
t.start()
while True:
    with lock:
        a += 1
        b += 1
t.join()

