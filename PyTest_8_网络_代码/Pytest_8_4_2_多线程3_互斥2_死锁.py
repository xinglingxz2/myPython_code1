''' 死锁 ：多线程保持自有数据不释放，并争夺对方数据，造成程序堵塞。
  造成死锁原因：1.单线程内 嵌套锁定对象，多次锁同一对象会阻塞。
            2.多线程内 同时先锁定自身资源，又争夺对方资源，造成阻塞。

   解决方法： 1. 使A线程等待执行完毕，再执行B线程。错开同时执行
            2. 使用定时锁
            3. 使用重入锁RLock()，使用方法同Lock()

'''

from threading import Thread, Lock
import time

# 交易类
class Account:
    def __init__(self,_id,balance,lock):
        self.id = _id # 用户
        self.balance = balance # 存款额
        self.lock = lock  # 把锁对象传入

    # 取钱
    def withdraw(self,amount):
        self.balance -= amount

    # 存钱
    def deposit(self,amount):
        self.balance += amount

    # 查看存款
    def get_balance(self):
        return self.balance

# 转账函数
def transfer(from_,to,amount):
    # 上锁成功返回True
    if from_.lock.acquire(): # 锁住自己的存款额
        from_.withdraw(amount)  # 减少自己存款金额
        # time.sleep(0.5) # *** 此处延时死锁 （让A线程执锁等待的时候，B线程也锁住自己，）
        if to.lock.acquire(): # 锁住对方的存款额
            to.deposit(amount) # 增加对方存款额
            to.lock.release()  # 对方账户解锁
        from_.lock.release() #自己账户解锁
    print("转账完成")

#------------------------------------------------

Abobi = Account("Abobi",5000,Lock())  # 参3：为自己对象 创建的 Lock锁对象
Mary = Account("Mary",7000,Lock())

t1 = Thread(target=transfer,args=(Abobi,Mary,1500))
t2 = Thread(target=transfer,args=(Mary,Abobi,500))
t1.start()
time.sleep(2)  # 解决死锁 （让A线程执行完，B线程再执行，错开同时执行）
t2.start()

t1.join()
t2.join()
print("Abobi $: %d",Abobi.get_balance())
print("                     Mary $: %d",Mary.get_balance())
