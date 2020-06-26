class Queue:
    def __init__(self):
        self.enteries=[]
        self.length=0
        self.front=0

    def __str__(self):
        printed="<"+str(self.enteries)[1:-1]+">"
        return printed

    # 入队
    def put(self,item):
        self.enteries.append(item)
        self.length +=1

    # 出队,先进先出
    def get(self):
        self.length=self.length-1
        dequeued=self.enteries[self.front]
        self.enteries=self.enteries[1:]
        return dequeued

    def front(self):
        return self.enteries[0]

    def size(self):
        return self.length

q=Queue()
q.put(1)
q.put(2)
q.put(5)
print(q)
q.get()
print(q)
print(q.front)
print(q.size())