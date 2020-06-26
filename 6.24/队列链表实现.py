from typing import Any,Optional
class Node:
    def __init__(self,data:Any,next:Optional=None):
        self.data:Any=data
        self.next:Optional=next

    def __repr__(self):
        return f"Node({self.data})"

class LinkedQueue:
    def __init__(self)->None:
        self.front:Optional[Node]=None
        self.rear:Optional[Node]=None
        self.size=0

    def put(self,item:Any)->None:
        node:Node=Node(item)
        if self.is_empty():
            self.front=node
            self.rear=node
        else:
            assert isinstance(self.rear,Node)
            self.rear.next=node
            self.rear=node
            self.size +=1

    def pop(self):
        if self.is_empty():
            raise IndexError("empty queue")
        else:
            node:Node=self.front
            self.front=node.next
            self.size -=1

    def is_empty(self)->bool:
        return self.front is None

    def get(self)->Any:
        if self.is_empty():
            raise IndexError("get from empty queue")
        else:
            assert isinstance(self.front,Node)
            node:Node=self.front
            self.front=node.next
            if self.front is None:
                self.rear=None
            return node.data

    def __repr(self):
        current=self.front
        string_repr=""
        while current:
            string_repr +=f"{current}<--"
            current=current.next
        return string_repr+"END"

if __name__ == '__main__':
    queue = LinkedQueue()
    queue.put(1)
    queue.put(2)
    queue.put('good')
    queue.put('nihao')
    print(queue)

