from typing import Any


class Quee:

    def __init__(self) -> None:
        self.quee_list=[]


    def push(self,new_member:Any)->None:
        self.quee_list.append(new_member)

    def pop(self)->Any:
        return self.quee_list.pop(0)

    def __str__(self) -> str:
        return str(self.quee_list)


