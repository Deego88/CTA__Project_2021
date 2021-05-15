def insertionSort(myArray):
    # take second element and store it in a variable
    for step in range(1, len(myArray)):
        key = myArray[step]
        j = step - 1

        # Compare variable with each element on the left of it until an element smaller than it is found
        # For descending order, change variable < myArray[j] to variable > myArray[j]
        while j >= 0 and key < myArray[j]:
            myArray[j + 1] = myArray[j]
            j = j - 1

        # Place variable after the element just smaller than it
        myArray[j + 1] = key


data = [22, 55, 91, 15, 66, 22, 25, 5, 18]
insertionSort(data)
print('Sorted myArray in Ascending Order:')
print(data)
