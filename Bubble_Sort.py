# Bubble sort function in Python
def bubbleSort(myArray):
 # loop over the length of the input array each element
    for passnum in range(len(myArrray)-1,0,-1):
      # loop over elements and compare array elements
        for i in range(passnum):
          # compare two adjacent elements
          # change > to < to sort in descending order
            if myArrray[i] > myArrray[i+1]:
               # swapping elements if elements
               # are not in the intended order
                temp = myArrray[i]
                myArrray[i] = myArrray[i+1]
                myArrray[i+1] = temp
myArrray = [22,55,91,15,66,22,25,5,18]
bubbleSort(myArrray)
print(myArrray)


