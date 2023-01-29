'''    互斥（互相排斥，保证只有1个线程 修改同一共用数据， 保证数据不紊乱。）
互斥1： Event  （ 线程间 是都可以 设置阻塞，或设置解除阻塞的。）
  e = Event()  # 创建Event对象
  e.wait([timeout])  # 阻塞等待 e被重新set， 超时 也解除阻塞
  e.set()  # 设置e  结束wait阻塞  解除    返回 None
  e.clear()  # e回到未设置状态
  e.is_set()  # 查看当前e是否被设置

互斥2： Lock  线程锁

'''
# ------------   互斥1： Event  事件  -------------------
from threading import Event ,Thread   # 导入
from time import sleep
'''
e= Event() # 创建Event对象
e.wait(3)  # 设置等待3秒
e.set() # 解除等待
'''

s = None  # 全局变量 用于通信
e= Event()  # 1.创建Event对象

def 杨子():
    print("杨子前来拜山头")
    global s
    s= "天王盖地虎"
    e.set()  # 3. 子线程 解除等待

t = Thread(target=杨子)
t.start()

print("请回口令...")
e.wait() # 2. 主线程 设置等待
if s == "天王盖地虎":
    print("BTZHY")
    print("OK yes ")
else:
    print("已经被打死")



t.join()

