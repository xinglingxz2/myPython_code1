'''

   target ：  目标数组
   item  ：   目标数组 其中的1个元素   （可以在 条件函数 内，再次指定其中的 实例数据. 例：func_condition(target[item])）
'''


class listHelper:
    @staticmethod
    def find_all(target,func_condition):
        # 查找列表中满足条件的所有元素。  参1：列表   参2：条件函数
        for item in target:
            if func_condition(item):
                yield item

    # @staticmethod
    # def first(target,func_condition):



    @staticmethod
    def select(target,func_condition):
        # 筛选列表中指定条件的数据
        for item in target:
            yield func_condition(item)

    @staticmethod
    def sum(target,func_condition):
        # 求列表中指定条件的所有元素和。  参1：列表   参2：条件函数
        sum_value =0
        for item in target:
            sum_value = func_condition(target[item]) + sum_value   # 或是 sum_value += func_condition(item)
        return  sum_value

    # @staticmethod
    # def last(target,func_condition):

    # @staticmethod
    # def get_count(target,func_condition):

    @staticmethod
    def get_max(target,func_condition):
        max = target[0]   # 传入的 是对象列表的 首元素
        for item in range(1,len(target)):
            if  func_condition(max) < func_condition(target[item]):  # 原来错误的    if max[item] < func_condition(item):   // 正确的： if func_condition(max) < func_condition(target[item]):
                max = target[item]
        return  max


    @staticmethod
    def order_byOld(target,func_condition):
        # 根据列表相关元素的大小排序。  参1：列表   参2：条件函数  # 升序 改变原始目标顺序
        for r in range(len(target)-1):
            for c in range( r+1,len(target)):
                if func_condition(target[r]) > func_condition(target[c]):
                    target[r],target[c] = target[c],target[r]

    @staticmethod
    def order_byNew(target,func_condition):
        # 根据列表相关元素的大小排序。  参1：列表   参2：条件函数  # 升序 返回创建的新目标
        newLine = []
        newLine.append(target[0])
        for r in range(len(target)-1):
            for c in range( r+1,len(target)):
                if func_condition(target[r]) > func_condition(target[c]):  #???????
                    # target[r],target[c] = target[c],target[r]
                    newLine.append(target[c])
                else:
                    newLine.insert(len(newLine),target[c])
        return newLine