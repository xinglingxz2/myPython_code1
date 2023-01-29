# 1）	函数式编程  // 函数可以被当成参数
# 2）  lambda 匿名函数  // 定义： lambda 形参 ：方法体

list1=[2,53,46,77,12,19,60,1,16,9]
def find_all (target, func_condition):
    for item in target:
        if func_condition(item):
            yield item

def condition01(item):
    return item > 9

for item in find_all(list1,condition01): # 此处不带（），
    print (item)

for item in find_all(list1,lambda item : item > 9):  # lambda 匿名调用
    print (item)

list1=[2,53,46,77,12,19,60,1,16,9]
list2=['A','B','C','D','E','F','G',]
list3 =[]
for item in zip(list2,list1):
    list3.append(item)
print (list3)