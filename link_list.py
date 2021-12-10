from typing import Optional


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


class LinkedList:

    def __init__(self) -> None:
        self.root: Optional[Element] = None

    def _add_node(self, node):
        pass
  

    def add_begin(self, node: Element) -> None:
        if not node.is_free():
            raise Exception("elemebt must be free!")

        if self.root is None:
            self.root = node
        else:
            node.next = self.root
            self.root = node
            node.add_to_linked_list()


    def __len__(self):
        counter=1
        temp=self.root
        while temp.next:
            counter+=1
            temp=temp.next            
        return counter
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
            


    def pop(self) -> Element:
        if self.root==None:
            raise Exception("khali ast!!!!!!")

        else:
            temp=self.root
            while temp.next :
                temp1=temp
                temp=temp.next
            temp1.next=None
            temp1.free_from_linked_list()

    def search(self, node: Element) -> bool:
        temp = self.root
        counter=0
        while temp.next:
            if temp is node:
                return counter
            else:
                temp=temp.next
                counter+=1
        else:
            return -1

    def add_between(self, node1: Element, new_node: Element):
        temp=self.root
        while temp.next:
            if temp is node1:
                temp1=temp.next
                temp.next=new_node
                new_node.next=temp1
                break
            else:
                temp=temp.next


    def remove(self, node: Element):
        temp = self.root
        temp_prev=None
        while temp.next:
            if temp is node:
                if temp_prev:
                    temp1=temp.next
                    temp_prev.next=temp1
                    break
                else:
                    self.root=temp.next

        return False
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
elm5=Element("abas")
elm4 = Element("mapsa")
l1 = LinkedList()
l1.add_begin(elm1)
l1.add_begin(elm2)
l1.add_begin(elm3)
l1.push(elm5)


