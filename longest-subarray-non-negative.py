def nonNegative(arr):
    length_Of_Original_Array=len(arr)
    firstArr=[0] * (length_Of_Original_Array+1)
    secondArr=[0] * (length_Of_Original_Array+1)
    left=-1
    right=-1
    for index in range(0,length_Of_Original_Array):
        firstArr[index+1]=firstArr[index] + arr[index]
        if firstArr[index] < firstArr[secondArr[index]]:
            secondArr[index+1]=index
        else:
            secondArr[index+1]=secondArr[index]
        aux=index-right+left
        while aux>0:
            if (firstArr[index+1]-firstArr[secondArr[aux]]) >= 0:
                aux=secondArr[aux]-1
            else:
                break
            left=aux+1
            right=index
    return arr[left:right+1]

if __name__ == "__main__":
    testcases = [
        [[100,100,-100]],
        [[-1,-1,-1]],
        [[5,-5,5]],
        [[5,0,0,0]],
        [[2,2,-11,2,2,2]],
        [[1,-1,-1]],
        [[1000,-1000,1000,-1000,2000]]
    ]
    for test in testcases:
        print("Longest contiguous sub-array in ", test, " is ",nonNegative(test[0]))
