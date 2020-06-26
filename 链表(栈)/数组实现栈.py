class stack:
    # 设置初始函数,设置空列表,大小为0
    def __init__(self,limit=10):
        self.stack=[]
        self.size=0

    # 布尔函数,判断是否为空,空为False,非空为True
    def __bool__(self):
        return bool(self.stack)

    # 列表以字符串形式表示
    def __str__(self):
        return str(self.stack)

    # 压栈,大小+1
    def push(self,data):
        self.stack.append(data)
        self.size +=1

    # 弹栈,若非空就弹出,空列表则触发错误,先进后出,弹出最后一位
    def pop(self):
        if self.stack:
            temp=self.stack.pop()
            self.size -=1
            return temp
        else:
            raise IndexError("pop from an empty stack")

    # 返回顶部元素,不是空列表就返回最后一位
    def peek(self):
        if self.stack:
            return self.stack[-1]

    # 是否为空列表,调用布尔函数,空返回True,非空返回False,跟布尔完全相反
    def is_empty(self):
        return not bool(self.stack)

    # 判断大小
    def size(self):
        return self.size

if __name__ == '__main__':
    stack=stack()
    for i in range(10):
        stack.push(i)
    print(stack)
    stack.pop()
    print(stack)
    print(stack.peek())
    print(stack.size)
    print(stack.is_empty())