class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue(object):
    def __init__(self):
        self.front=None
        self.rear=None
    def empty_check(self):
        if self.front==None:
            return
    def Add_To_Queue(self,data):
        newnode=Node(data)
        if self.front==None:
            self.front=newnode
            self.rear=newnode
            return
    def dequeue(self):
        if self.empty_check():
            print('queue is empty')
            return
        else:
            temp=self.front
            self.front=temp.next
        if self.front==None:
            self.rear=None
            return


q=Queue()
q.Add_To_Queue(10)
q.Add_To_Queue(15)
q.Add_To_Queue(20)
q.Add_To_Queue(25)
print(str(q.front.data))
q.dequeue()
# print(str(q.front.data))
print(str(q.rear))


