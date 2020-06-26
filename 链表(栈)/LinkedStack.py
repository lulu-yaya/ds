from typing import Any,Optional,NoReturn
# 导入tying包和数据类型

# 设置初始函数和表达方式
class Node:
    # Any指任意类型,Optional为可选类型,先设置为空
    def __init__(self,data:Any,next:Optional=None):
        self.data:Any=data
        self.next:Optional[Node]=next

    def __repr__(self):
        return f"Node({self.data})"
        # 字符串格式化输出

# 建立链表的栈,设置头部用top,类型为NoReturn，表示可空可节点
class LinkedStack:
    def __init__(self)->NoReturn:
        self.top=None
        self.size=0

    # 写push插入，新创建一个Node，若顶部为空，则顶部节点为新建的node，若顶部不为空，node的下一个为top
    def push(self,item:Any)->None:
        node=Node(item)
        if self.top is None:
            self.top=node
        else:
            node.next=self.top
            self.top=node
        self.size +=1

    # 弹出函数pop，若为空，弹出错误，如果不是空，就弹出顶部，然后重新指定顶部，返回删除后的data
    def pop(self)->Any:
        if self.top is None:
            raise IndexError("pop from empty stack")
        else:
            node:Node=self.top
            self.top=node.next
            self.size -=1
            return node.data

    # 是否为空
    def is_empty(self) ->bool:
        return self.top is None

    def capacity(self):
        return self.size

    def __repr__(self):
        current=self.top
        string_repr=""
        while current:
            string_repr +=f"{current} -->"
            current=current.next
        return string_repr +"END"

if __name__ == '__main__':
    stack=LinkedStack()
    stack.push(5)
    stack.push(9)
    stack.push('python')
    print(stack)
    print(stack.size)
    stack.pop()
    print(stack)
    print(stack.capacity())
    print(stack.is_empty())