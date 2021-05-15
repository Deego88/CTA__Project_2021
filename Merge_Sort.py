def mergeSort(myArray):
    # print to show splitting 
    print("Splitting ",myArray)
    # if array is greater than 1 then:
    if len(myArray) > 1:
        # mid, leftside, and right side of array stored as variables
        mid = len(myArray)//2
        lefthalf = myArray[:mid]
        righthalf = myArray[mid:]
        # function mergeSort passed both sides of array
        mergeSort(lefthalf)
        mergeSort(righthalf)
        # initialise 
        i=0
        j=0
        k=0
        # while loop, while i less than the length of leftside of array and right side of the array do the following
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                myArray[k] = lefthalf[i]
                i=i+1
            else:
                myArray[k] = righthalf[j]
                j = j+1
            k = k+1
        # while loop, while i less than the length of leftside of array do the following
        while i < len(lefthalf):
            myArray[k] = lefthalf[i]
            i = i+1
            k = k+1
        # while loop, while j less than the length of rightside of array do the following
        while j < len(righthalf):
            myArray[k] = righthalf[j]
            j = j+1
            k = k+1
    # print to show merging 
    print("Merging ",myArray)

myArrray = [22,55,91,15,66,22,25,5,18]
mergeSort(myArrray)
print(myArrray)