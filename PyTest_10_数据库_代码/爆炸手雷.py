import sys



    #   C:\Users\Administrator\PycharmProjects\
    # """
    # 设计思想 ： 使用（中间调用类）间接调用其 子类（接口类）
    #
    #   此程序使用的是依赖，
    #   泛化：（继承）
    #   关联：B类为A类的成员数据
    #   依赖：B类为A类的方法的参数
    #
    # """


class ShouLei:  # 手雷 类
    def startBao(self,anyone,lose_blood): #启动爆炸 方法 （参数：
        if not isinstance(anyone,BaoZa):  #如果传入的对象，不是爆炸类（中间调用类），则退出
            return
        anyone.injure(lose_blood)


class BaoZa:   #爆炸类 （中间调用类） //父类
    def injure(self,lose_blood):  #伤害方法： 参数：流血值
        raise NotImplementedError()   # 没有实现报错误 ：提醒子类实现 这方法

class Person (BaoZa):  #人类 （继承 爆炸类）
    def __init__(self,name):
        self.__name = name
    def injure(self,lose_blood):   #  //子类 复写父类方法，
        print(self.__name + "流淌了%d滴血"%(lose_blood))

class Animals (BaoZa):  #动物类
    def __init__(self,ani_name):
        self.__name = ani_name
    def injure(self,lose_blood):
        print(self.__name + "流淌了%d滴血"%(lose_blood))


#/////////////////////////////////////////////////#

# if __name__ =="__main__":
#     view = ()

showlei1 = ShouLei()

p1= Person("张三")
showlei1.startBao(p1,9)


