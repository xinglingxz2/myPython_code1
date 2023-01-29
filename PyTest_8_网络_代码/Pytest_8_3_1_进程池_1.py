''' 进程池 实例 成功演示

'''

from multiprocessing import Pool  # 1.导入进程池
from time import sleep

def worker(msg):
    sleep(2)
    print(msg)

# 2.创建进程池
pool = Pool()

# 3.向进程池添加事件
for i in range(20):
    msg = "hello %d"%i
    pool.apply_async(func = worker,args = (msg,))

# 4.关闭进程池
pool.close()

# 5.回收进程池
pool.join()


