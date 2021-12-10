
def divisible(input_number:str)->int:

    count = 0
    if input_number[0]=="0" and len(input_number)>1:
        return count

    elif "_" in input_number:
        for i in range(0,10):
            index = input_number.find("_")
            new = input_number[:index] + str(i)+input_number[index+1:]
            count +=divisible(new)

    elif "X" in input_number:
        for n in range(0,10):
            new = input_number.replace("X",str(n))
            count += divisible(new)

    else :
        if  not int(input_number)%25:
            count+=1  
 

    return count

input_1 = input()
print(divisible(input_1))