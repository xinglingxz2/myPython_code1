'''    例程实现
  多线程1 .基本创建
属性： name=   .setname     .getName()获取名称    t.is_alive() 是否在t线程的生命周期内，返回Ture或Flase
     .daemon    .setDaemon()  .isDaemon() # True 主线程退出，子线程也退出
      #第三方插件  threadpool
python GIL
结论： Python多线程 对于计算密集型程序 不会提高速度。但对于IO延迟等待型程序，会有提速。
     多进程的速度要快于多线程。 进程消耗资源要比线程多。
     进程空间数据互不干扰，有专门通信方式，线程用全局变量通信，通信时注意同步互斥
'''

import threading
from time import sleep


def music(name):
    for i in range(20):
        sleep(1)
        print("play music %s for you   "%name,i)

t = threading.Thread(target=music,args=("xingrushui",) ,name="TT")  # 设置线程名称TT
t1 = threading.Thread(target=music,args=("mengtuoling",))
t.start()
t1.start()
t1.join()
t.join()



