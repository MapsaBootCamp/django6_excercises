from typing import Any


class Stack:

    def __init__(self) -> None:
        self.stack_list=[]


    def push(self,new_member:Any)->None:
        self.stack_list.append(new_member)

    def pop(self)->Any:
        return self.stack_list.pop()

    def __str__(self) -> str:
        return str(self.stack_list)


