# G00387896 Ricahrd Deegan

# Import libraries

from Selection_Sort import selectionSort
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time as time
from random import randint

# five algorithms to be used, 1.bubbleSort, 2.mergeSort, 3.selectionSort, 4.insertionSort and 5.countingSort sort.
myArrray = [22, 55, 91, 15, 66, 22, 25, 5, 18]


# bubbleSort.[1]
def bubbleSort(myArray):
 # loop over the length of the input array each element- outter loop
    for passnum in range(len(myArrray)-1, 0, -1):
      # loop over elements and compare array elements- inner loop
        for i in range(passnum):
          # compare two adjacent elements
          # change > to < to sort in descending order
            if myArrray[i] > myArrray[i+1]:
               # swapping elements if elements
               # are not in the intended order
                temp = myArrray[i]
                myArrray[i] = myArrray[i+1]
                myArrray[i+1] = temp
            return myArray


# mergeSort. [2]
def mergeSort(myArray):
    # print to show splitting
    print("Splitting ", myArray)
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
        i = 0
        j = 0
        k = 0
        # while loop, while i less than the length of leftside of array and right side of the array do the following
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                myArray[k] = lefthalf[i]
                i = i+1
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
        return myArray

    # selectionSort. [3]

    def selectionSort(myArray):
     # loop over the length of the input array each element
        for fillslot in range(len(myArray)-1, 0, -1):
            # set max position and for loop with conditional statement
            positionOfMax = 0
            for location in range(1, fillslot + 1):
                if myArray[location] > myArray[positionOfMax]:
                    positionOfMax = location
        # element swap
            temp = myArray[fillslot]
            myArray[fillslot] = myArray[positionOfMax]
            myArray[positionOfMax] = temp
        return myArray


# insertionSort. [4]
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
    return myArray


# countingSort.[5]
def countingSort(myArray):
    # set max value to 0
    # find max vlaue in array and assign bucket to according to max value
    maxValue = 0
    for i in range(len(myArray)):
        if myArray[i] > maxValue:
            maxValue = myArray[i]

    buckets = [0] * (maxValue + 1)
    # iterate input array and increment everytime an item appears
    for i in myArray:
        buckets[i] += 1
    # from smallest to largest value add index of the bucket to the input array
    # and decrease the counter in the bucket in question by 1, until counter is zero
    i = 0
    for j in range(maxValue + 1):
        for a in range(buckets[j]):
            myArray[i] = j
            i += 1
    return myArray


#  function for generating test arrays
def array_test(size):
    # return array of the selected size
    return [np.random.randint(1000) for i in range(size)]

# Timer Function for running time
def timer(input_array, sort_algo):
    start = time.time()
    sort_algo(input_array)
    end = time.time()
    return (end-start)

# Timer Function for average running time
def ave_runtime(num_runs, size, sort_algo):
    # Empty array to store results
    trial_times = []
    # While loop that runs the algorithm a set  number of times
    counter = 0
    while counter < num_runs:
        input_array = array_test(size)
        trial_times.append(timer(input_array, sort_algo))
        counter = counter + 1
    # return average runtime of the algorithm
    return (sum(trial_times)/len(trial_times))

# Section 4 - Formatting the output

# create a function to carry out the trials [6]
def algo_trial(algo, test_size):
    # Get the averge run time of an algoritm and test size that is ran 10 times
    return float("{:10.3f}".format(ave_runtime(10, test_size, algo)*1000))

# Function to create col
# Algo and test size passed in as arguments
def col_create(algos, test_size):
    # For loop tests each algorithm for the test size
    col = []
    for i in algos:
        col.append(algo_trial(i, test_size))
    # return results 
    return(col)

# Create DataFrame function and pass a dict to the function
def df_create(data_dict):
    # Create the DF and select the index to be the the size field
    data = pd.DataFrame(data_dict)
    data.set_index("size", inplace=True)
    # Retrun the data
    return data

#
# References
# [1] https://www.studytonight.com/data-structures/bubble-sort
# [2] http://www.openbookproject.net/books/pythonds/SortSearch/TheMergeSort.html
# [3] https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheSelectionSort.html
# [4] https://www.freecodecamp.org/news/sorting-algorithms-explained-with-examples-in-python-java-and-c/
# [5] https://www.happycoders.eu/algorithms/counting-sort/
# [6] https://thepythonguru.com/python-string-formatting/
