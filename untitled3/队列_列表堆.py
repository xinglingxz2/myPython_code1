'''

'''

# 自定义异常
class StackError(Exception):
    pass

# 基于列表实现顺序
class LStack:
    def __init__(self):
        self._elems = []  #列表的第一个元素为堆顶， 最后一个为堆底

      # 显示堆顶的元素
    def top(self):
        if not self._elems:
            raise StackError("stack is empty")
        return self._elems[0]

    # 判定栈是否为空
    def is_empty(self):
        return  self._elems == []

    # 入堆
    def push(self,elem):
        self._elems.append(elem)

    # 出堆
    def pop(self):
        if not self._elems:
            raise StackError("stack is empty")
        return self._elems.pop(0)



#  ============================================================
if __name__ == "__main__":
    st = LStack()  # 初始化栈
    print(st.is_empty())
    st.push(10)
    st.push(20)
    st.push(30)
    while not st.is_empty():
        print(st.pop())
