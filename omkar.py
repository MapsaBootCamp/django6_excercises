def omkar(matris,opt1,opt2):
    new_matris=partition(matris,int(opt1)-1,int(opt2))
    for i in range(len(new_matris)):
        if "X." in new_matris[i]:
            if i==0:
                continue
            else:
                loc=new_matris[i].find("X.")+1
                for j in range(0,i):
                    if new_matris[i-1][loc] == "X":
                        return False
    return True
        
def partition(matris,obj1,obj2):
    new_matris=[]
    for i in range(len(matris)):
        new=""
        for j in range(obj1,obj2):
            new+=matris[i][j]
        new_matris.append(new)

    return new_matris
    
if __name__ == "__main__":
    row=int(input("row:"))
    column=int(input("columen:"))
    matris=[]
    for i in range(row):
        second_mat=[]
        for j in range(column):
            second_mat.append(input(":"))
        matris.append(second_mat)


    time=int(input("chand bar:"))
    for i in range(time):
        opt1=input("1:")
        opt2=input("2:")
        if omkar(matris,opt1,opt2):
            print("YES")
        else:
            print("NO")


    

