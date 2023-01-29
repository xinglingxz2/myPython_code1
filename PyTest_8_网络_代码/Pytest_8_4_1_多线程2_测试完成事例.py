'''
多线程2：    完成自定义多线程，使其能够自动运行player函数
'''
from threading import Thread
from time import *

class MyThread(Thread):
    # 参数2：使用函数式编程，最终调用时指定。
    # 参数如要可有可无，型参就要赋默认值，哪怕为空，下列为各种空赋值。
    def __init__(self,target=None,args=(),kwargs={},name=""):
        super().__init__()
        self.target= target
        self.args = args
        self.kwargs = kwargs
        self.name = name
    def run(self):
        self.target(*self.args,**self.kwargs)
    #^  target参数名当型参，与player函数实参名替代。
        # 类内生明皆为型参。直接指向调用函数 的型参是真实参的参数类型
#=================================================

def player(sec,song):
    for i in range(2):
        print("Playing %s:%s"%(song,ctime()))
        sleep(sec)

t = MyThread(target=player,args=(3,),
             kwargs={'song':"凉凉"},name ="happy")
t.start()
t.join()



