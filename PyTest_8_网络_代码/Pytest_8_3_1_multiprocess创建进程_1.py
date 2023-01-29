'''    实例 成功演示
multiprocessing 模块创建进程
 特点：  1。 子进程必须封装为函数
        2   使用Process()类创建进程对象
                 参数：target (必须的）绑定指定的目标函数；
                       args=(元祖)： 给目标函数 位置传参  (1,)
                       kwargs=字典：给目标函数 键值传参 {'字符串类型键名':xxx}
        3   使用start启动进程，
        4   使用 join回收进程

 优点： 可以轻易的创建多个子进程
 缺点：不能使用标准输入流
   进程对象的属性： p.name  设置名称;   | p.pid  进程PID号 ; | p.is_alive() 是否在生命周期内  ;
             |  p.daemon 设置父子进程退出关系： Ture 随父退出。
'''

import multiprocessing as mp
from time import *

# 封装的子进程函数
def childFun(x):
    for i in range(x):
        sleep(2)
        print("time = ", ctime())  # 时间函数 的 返回值类型不定


# 创建进程对象
p = mp.Process(target = childFun,args=(4,))  #  kwargs={'x':4}

p.start()   # 启动进程

# ---  此处可以添加父进程   ----#


p.join()    #回收进程




