from typing import Optional, Sized
from typing import Any


class Element:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.free = True

    def add_to_linked_list(self):
        self.free = False

    def free_from_linked_list(self):
        self.free = True
        self.next = None

    def is_free(self):
        if self.free:
            return True
        else:
            return False
    
    def __str__(self,) -> str:
        result  = "["
        result+=str(self.data)+"]"
        return result

class LinkedList:

    def __init__(self) -> None:
        self.root: Optional[Element] = None

    def add_begin(self, node: Element) -> None:
        if not node.is_free():
            raise Exception("elemebt must be free!")

        if self.root is None:
            self.root = node
            node.add_to_linked_list()
        else:
            node.next = self.root
            self.root = node
            node.add_to_linked_list()


    def __len__(self):
        count = 0
        if self.root is None:
            return count
        else:
            temp = self.root
            count+=1
            while temp.next:
                count+=1
                temp = temp.next
        return count




    def push(self, node: Element) -> None:
        if self.root is None:
            self.root = node
            node.add_to_linked_list()
        else:
            temp = self.root
            while temp.next:
                temp = temp.next
            temp.next = node
            node.add_to_linked_list()

    def pop(self) -> None:
        if self.root is None:
            raise Exception("linked list has no Elemnt")
        else:
            temp = self.root
            while temp.next:
                temp1 = temp
                temp = temp.next
            temp1.next = None
            temp.free_from_linked_list()
        return temp
            

    def search(self, node: Element) -> bool:
        if node.free :
            return False
        else:
            temp = self.root
            while temp:
                if temp is node:
                    return True
                else:
                    temp = temp.next
            return False

    def add_between(self, new_node: Element, node1: Element):
        if not new_node.free :
            raise Exception("new_node must be free")
        else:
            new_node.next = node1.next
            node1.next = new_node 
            new_node.add_to_linked_list()



    def __str__(self) -> str:
        result = "["
        if self.root is None:
            result += "]"
            return result
        else:
            result += str(self.root.data)
            temp = self.root
            while temp.next:
                result += "-> "
                temp = temp.next
                result += str(temp.data)
            result += "]"
        return result


elm1 = Element(2)
elm2 = Element("salam")
elm3 = Element([1, 2, 3])
elm4 = Element("hi")
        

l1 = LinkedList()
l1.add_begin(elm1)
l1.add_begin(elm2)
l1.add_begin(elm3)
print(l1)
l1.remove(elm1)
print(l1)