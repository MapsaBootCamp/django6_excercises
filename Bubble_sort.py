


numbers=[230,100,900,9,6,12,3,9,11,21,5,18,20,21,29,0,11,60,32,91]


length=len(numbers)-1

def bubbleSort(list_of_num):

    for i in range(length):

        for x in range(length):

            if numbers[x]>numbers[x+1]:
                numbers[x+1],numbers[x]=numbers[x],numbers[x+1]
    print(numbers)

bubbleSort(numbers)
