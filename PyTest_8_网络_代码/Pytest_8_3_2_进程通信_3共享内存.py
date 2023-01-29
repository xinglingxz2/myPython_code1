'''  共享内存  实例 成功演示，   特点： 速度快 ，进程间有关系
   共享内存1  Value （单值型的）,
       使用： obj = Value(ctype,data)  返回:共享内存对象
                参1：类型为 'i'整型 ; 'f'浮点型 ; 'c' 字符型;
                参2： 初始值 必须写入  。  value属性读写

   共享内存2  Array（多值列表型的）  索引读写(可迭代对象)
       使用： obj = Array(ctype,data)  返回:共享内存对象
                参1：类型为 'i'整型 ; 'f'浮点型 ; 'c' 字符型;
                参2： 整数：开辟空间的大小。
                     其他类型：存储的数据，如 b(hello)字节串; [1,2,3]列表;等  只能存字节串
       实例：#2指定1  shm = Array('i',[0,0,0,0,1]) #指定2 shm = Array('c',b"hello")
            #3修改  shm[1] = 60    # shm = b"world"  # shm[0] = b'H'
            #整体读取 .value属性    print(shm.value)  只能用于字符类型，输出字节串
'''


# 1.导入
from multiprocessing import Value ,Array    # 1.导入
from multiprocessing import Process  # 导入多进程
import time
from random import randint  # 导入随机整数


# 2.开辟共享内存，指定存储类型
money = Value('i',500)

# 3. 读写
def man():
    for i in range(30):
        time.sleep(0.2)
        money.value += randint(1,1000)  # 3.写入共享内存
        print("man存储了: ", money.value)

def girl():
    for i in range(30):
        time.sleep(0.2)
        money.value -= randint(1,800)
        print("          girl消费了:",money.value)

p1 = Process(target= man)
p2 = Process(target= girl)

p1.start()   # 启动进程
p2.start()

p1.join()  # 回收进程
p2.join()

print("现有余额： ",money.value)  # 读取共享内存