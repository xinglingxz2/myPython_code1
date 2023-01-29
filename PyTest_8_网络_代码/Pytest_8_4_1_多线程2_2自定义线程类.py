'''  自定义线程类：     例程实现
创建： 1,继承Thread类，2.重写__init__方法添加自己属性，使用super加载父类属性
      3. 重写run方法
使用： 1.实例化对象，2.调用start自动运行run方法。3.调用join回收线程
'''

from threading import Thread

class MyThreadClass(Thread):
    def __init__(self,attr):
        super().__init__()  # 调用父类的初始化函数  super(参1：继承类名:MyThreadClass， 参2：实例化对象名:self)。 类内调用可省略参数
        self.attr = attr  # 添加新的自己属性

    def f1(self):  # 类内其他配合方法
        print("步骤1的具体内容。。。")

    def f2(self):
        print("步骤2的具体内容。。。",self.attr)

    def run(self):  # 调用线程自动的方法
        self.f1()
        self.f2()

t = MyThreadClass("start my Thread")  # 1.实例化 自定义线程类对象
t.start() # 2.自动运行run方法
t.join()  # 3.回收线程