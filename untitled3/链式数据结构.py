'''
    1.结点：
    2.关联：
    3.实现的炒作：
'''

class A:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name




# 创建结点类：
class Node:
    def __init__(self,dataVal, nextAddress = None):
        self.dataVal = dataVal      # 有用数据
        self.nextAddress = nextAddress  # 下一结点地址

# 创建关联类：
class Linklist:
    def __init__(self,data):
        # self.head = None
        self.head = Node(None)  # 链表的开头  为结点类型   数据：= 空   地址：默认
        self.data = data
        self.__init_list(self.data)  # 初始化链表数据

    # 初始化链表数据
    def __init_list(self,length):
        #self.head = Node(None)  # 链表的开头  为结点类型   数据：= 空   地址：默认
        p = self.head   #  定义变量p ,赋值为 结点类型的 self.head
        for i in length:
            p.nextAddress = Node(i)  # p.next...存入 结点类型的i 的地址
            p = p.nextAddress   #  变量p 移动到下一个 列表元素

    def showData(self):
        d = self.head.nextAddress  # 相当于 1): d = self.hand    & 2):  d = d.nextAddress
        #print(p.)
        while d:
            print(d.dataVal, end = ';  ')
            d = d.nextAddress

    def append(self,item):   # 链表最后添加新元素
        p = self.head   #
        while p.nextAddress != None:
            p = p.nextAddress
        p.nextAddress = Node(item)

    def get_length(self):    # 获取链表长度
        n = 0
        p = self.head
        while p.nextAddress is not None:
            p = p.nextAddress
            n += 1
        return  n

    def is_empty(self):  # 判定列表是否为空
        if self.get_length() == 0:
            return True
        else:
            return False

    def clear(self):   # 清空列表
        self.head.nextAddress = None

    def get_one(self,item):  # 获取链表元素值于 item形参相等(值） 的元素
        p = self.head.nextAddress   #
        while p:
            if p.dataVal != item :
                p = p.nextAddress
            else:
                return p

    def get_item(self,x):  #   （自己写的）,
        '''
        获取链表的第x个元素
        :param x: 链表的序列号
        :return: 确定的元素，不是结点
        '''
        n = 0
        if x > self.get_length():
            raise IndexError("list index out of range")  # 主动报异常
        else:
            p = self.head.nextAddress
            while p:
                if n == x:
                    return p.dataVal
                else:
                    p = p.nextAddress
                    n += 1
        """
           教程源码：
             p = self.head.nextAddress
             i = 0
             while i < x and p is not None:
                i += 1
                p = p.nextAddress
            if p is None:
                raise IndexError("list index out of range")  # 主动报异常
            else:
                :return p.dataVal
        """

    def insert(self,index,data):
        '''
        在链表内，插入新元素
        :param index:  链表的序列号
        :param data: 需要插入的数值
        :return:
        '''
        if index < 0 or index > self.get_length(): # 如果不在范围内
            raise IndexError("list index out of range")
        else:
            p = self.head
            i = 0
            while i < index:
                p = p.nextAddress
                i += 1
            node = Node(data)
            node.nextAddress = p.nextAddress
            p.nextAddress = node

    # def delete_index(self,index):
    #     '''
    #     删除链表的第几个元素
    #     :param index: 链表的第几个序列号
    #     '''

    def delete_data(self,deldata):     # 删除链表内指定数据  ??????????? 有错误  可练习调试
        p = self.head.nextAddress   #  定义变量p ,赋值为 结点类型的 self.head  (p = 第一个元素）
        deln = Node(None)
        deln.nextAddress = p.nextAddress

        while p.nextAddress is not None:
            if p.dataVal == deldata:   # 如果第一个元素的数据 == 删除的数据
                deln = deln.nextAddress  # 后一个数据
                self.head.nextAddress = deln # 起始头元素的下一个地址（前一个地址） = （后一个头）
                break
            else:      # 第一个元素的数据 不等于
                for i in range(1,self.get_length()):
                    p = p.nextAddress    # 1
                    deln = p
                    print(i)
                    if  p.dataVal == deldata:  #     ????????????
                        deln = deln.nextAddress  # 后一个数据
                        self.get_one(i).nextAddress = deln  # 前一个元素的地址 =  后一个头
                        break
            break

    def delete_data_obj(self,deldata):   # 对象列表使用   # 删除链表内指定数据  ??????????? 有错误  可练习调试
            '''
                # 如果值相等则越过中间的结点
            :param deldata:
            :return:
            '''
            p = self.head
            p.nextAddress = p.nextAddress
            #while p.nextAddress is not None :
                #if  p.nextAddress.dataVal == deldata:
            for  i in range(self.get_length()):
                if  p.nextAddress.dataVal.name == deldata(self.data[0]):
                    p.nextAddress = p.nextAddress.nextAddress
                    break
                p = p.nextAddress
                i += 1
            else:
                raise ValueError("xdata not in list")
            # p = self.head.nextAddress   #  定义变量p ,赋值为 结点类型的 self.head  (p = 第一个元素）
            # deln = Node(None)
            # deln.nextAddress = p.nextAddress
            #
            # while p.nextAddress is not None:
            #     if A(p.dataVal[0]).name == deldata(self.data[0]):   # 如果第一个元素的数据 == 删除的数据
            #         deln = deln.nextAddress  # 后一个数据
            #         self.head.nextAddress = deln # 起始头元素的下一个地址（前一个地址） = （后一个头）
            #         break
            #     else:      # 第一个元素的数据 不等于
            #         for i in range(1,self.get_length()):
            #             p = p.nextAddress    # 1
            #             deln = p
            #             print(i)
            #             if  A(p.dataVal[i]).name == deldata(A(self.data[i])):  #     ????????????
            #                 deln = deln.nextAddress  # 后一个数据
            #                 self.get_one(i).nextAddress = deln  # 前一个元素的地址 =  后一个头
            #                 break
            #     break









        # if p.dataVal ==  Node(self.get_one(deldata)).dataVal:
        #     deln =deln.nextAddress


        # for i in self.data:
        #     if i.dataVal != deldata:
        #         p = i.nextAddress
        #     else:
        #         p = i
        #         p = p.nextAddress
        #         i.nextAddress = p.nextAddress






#======================================================
if __name__ =="__main__":
    link1 =[1,2,3,4,5,6]
    link2 = [A("张山"),A("力士"),A("王五"),A("赵六")]

    newl = Linklist(link2)
    newl.showData()

    print("--"*10)
    newl.append(A("韩小柒"))
    newl.showData()
    print("------------------**\n")

    print(newl.get_item(2))

    print(newl.get_length())
    newl.showData()
    print("-------!!!!----------\n")

    new2 = Linklist(link1)
    print(new2.get_one(5))
    new2.delete_data_obj(5)

    new2.showData()
    print("------------------))\n")

    newl.delete_data_obj(lambda item:item.name)
    newl.insert(3,A("赖小八"))
    newl.delete_data_obj(A("力士"))
    newl.showData()
1