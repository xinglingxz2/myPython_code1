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

# 基于链式 实现 栈
class LStack:
    def __init__(self):
        self._top = None  #标记栈顶位置

    def is_empty(self):
        return self._top is None

    def push(self,elem):  # 压栈
        # node = Node(elem)
        # node.nextAddress = self._top
        # self._top = node
        self._top = Node(elem,self._top)  # 3合1

    def pop(self):   # 弹栈
        if self._top is None:
            raise StackError("stack is empty")
        p = self._top
        self._top = p.nextAddress
        return p.dataVal

    def top(self):   # 栈顶 值
        if self._top is None:
            raise StackError("stack is empty")
        return self._top.dataVal



if __name__ =="__main__":
    st = LStack()
    print(st.is_empty())
    st.push(10)
    st.push(20)
    st.push(30)
    print(st.top())
    print(st.pop())
    print(st.pop())



