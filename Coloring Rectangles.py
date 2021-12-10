
def partiotion(lenght:int,height:int)->int:
    """
    @params:lenghth and height of rectangle (both int)

    @return:number of minimum blue

    """

    area=lenght*height
    counter=0
    while area>0:
        if area-3==0 or area-3>2:
            area-=3
            counter+=1

        else:
            area-=2
            counter+=1

    return counter


if __name__=="__main__":
    tedad=int(input())
    for i in range (tedad):
        print(partiotion(int(input()),int(input())))




