'''

'''

# 自定义异常
class StackError(Exception):
    pass

# 创建结点类：
class Node:
    def __init__(self,dataVal, nextAddress = None):
        self.dataVal = dataVal      # 有用数据
        self.nextAddress = nextAddress  # 下一结点地址

# 基于链式 实现 队列
class LQueue:
    def __init__(self):
        self._top = self._di = Node(None)  #标记堆顶位置

    def is_empty(self):
        return self._top == self._di

    def enterQueue(self,elem):  # 入队
            self._di.nextAddress = Node(elem)
            self._di =self._di.nextAddress

    def pop(self):   # 出队
        if self._top == self._di:
            raise StackError("stack is empty")
        self._top = self._top.nextAddress
        return self._top.dataVal

    def top(self):   # 堆顶 值
        p = Node(None)
        if self._top == self._di:
            raise StackError("stack is empty")
        else:
            p = self._top.nextAddress
            return p.dataVal



if __name__ =="__main__":
    st = LQueue()
    print(st.is_empty())
    st.enterQueue(10)
    st.enterQueue(20)
    st.enterQueue(30)
    print(st.pop())
    print(st.pop())
    print(st.pop())
