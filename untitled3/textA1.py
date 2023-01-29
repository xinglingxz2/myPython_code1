from list_tool import listHelper
from 链式数据结构 import *

class Man:
    def __init__(self,name,maney,xue):
        self.name = name
        self.maney = maney
        self.xue =xue

    def __str__(self):
        return  self.name

listA = [12,45,61,8,30,66,18,19,108,4,95,77]

listB = [Man("黄蓉",2000,36),Man("冷雨飘香",3800,82),Man("令狐冲",6500,78),Man("江小鱼",1300,99)]

listM =listHelper.order_byNew(listB, lambda e:e.maney)
for item in listM:
    print (item)
print("--"*16)


# he = listHelper.sum(listA,lambda e:e)
# print(he)

# yes = listHelper.sum(listB, lambda e: e.maney)
# print (yes)
# listHelper.order_by(listB,lambda e:e.maney)
# for item in listB:
#     print(item)

print(listHelper.get_max(listB,lambda e:e.maney))