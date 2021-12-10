
def taghsim(my_string:str)->int:

    count = 0
    if my_string[0]=="0" and len(my_string)>1:
        return count

    elif "_" in my_string:
        for i in range(0,10):
            index = my_string.find("_")
            new = my_string[:index] + str(i)+my_string[index+1:]
            count +=taghsim(new)

    elif "X" in my_string:
        for n in range(0,10):
            new = my_string.replace("X",str(n))
            count += taghsim(new)

    else :
        if  not int(my_string)%25:
            count+=1  
 

    return count

test = input()
print(taghsim(test))

