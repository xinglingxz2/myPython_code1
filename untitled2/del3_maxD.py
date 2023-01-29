'''
求列表内最大， 使用 函数式编程
'''

class A:
    def __init__(self,id,name,age):
        self.id =id
        self.name = name
        self.age =age
    def __str__(self):
        return  ("我是%s,我的年龄是%d"%(self.name,self.id))

listA = [23,43,56,17,90,72,88,60]
listB = [A(1,"张三",18), A(1,"李四",22), A(1,"王五",51)]

def max_data(target, xxx):
    max_d = target[0]
    for i in range(1,len(target)):    #   target(1,len(target)) //错误的：这里是 真实对象的 内部数据 ，下面要是的 目标的序列
        if xxx(max_d) < xxx(target[i]):       #    max_d.id  < target[i].id  // 只比较1种（id)的大小。
            max_d = target[i]

    print(max_d)
    return max_d

def xxx(item):
    return  item.age


# max_data(listB,xxx)    # 函数当参数使用 不用输入括号（）

max_data(listB,lambda item:item.id ) # 使用lambda匿名方法 调用
print(__name__)  # 返回本模块名 或__main__
print(__file__)  # 返回模块地址
print(__doc__)   # 返回模块文档注释
print(__all__)   # 定义可导出成员，仅对 form xx import * 语句有效

