def selectionSort(myArray):
     #loop over the length of the input array each element
   for fillslot in range(len(myArray)-1, 0, -1):
        #set max position and for loop with conditional statement 
       positionOfMax = 0
       for location in range(1, fillslot + 1):
           if myArray[location] > myArray[positionOfMax]:
               positionOfMax = location
        # element swap
       temp = myArray[fillslot]
       myArray[fillslot] = myArray[positionOfMax]
       myArray[positionOfMax] = temp
# array input 
myArrray = [22,55,91,15,66,22,25,5,18]
selectionSort(myArrray)
print(myArrray)