# G00387896 Ricahrd Deegan

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

# five algorithms to be used, 1.bubbleSort, 2.mergeSort, 3.selectionSort, 4.insertionSort and 5.countingSort sort.

# bubbleSort.[1]


def bubbleSort(myArray):
 # loop over the length of the input array each element- outter loop
    for passnum in range(len(myArray)-1, 0, -1):
      # loop over elements and compare array elements- inner loop
        for i in range(passnum):
          # compare two adjacent elements
          # change > to < to sort in descending order
            if myArray[i] > myArray[i+1]:
               # swapping elements if elements
               # are not in the intended order
                temp = myArray[i]
                myArray[i] = myArray[i+1]
                myArray[i+1] = temp
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
    # note that this is adapted code
    # i have hard coded 1000 in as the max value becase my array generator
    # creates lists of integers between 1 and 1000
    # create a counter array to count the number of instances of each number
    m = 1000 + 1
    count = [0] * m
    for a in myArray:
        # count occurences of each number in the array
        count[a] += 1
    i = 0
    # recreate the array using information from the count step
    for a in range(m):
        for c in range(count[a]):
            myArray[i] = a
            i += 1
    return myArray

#  function for generating test arrays [8]


def array_test(size):
    # return array of the selected size
    return [np.random.randint(1000) for i in range(size)]

# Timer Function for running time [6]


def timer(input_array, sort_algo):
    start = time.time()
    sort_algo(input_array)
    end = time.time()
    return (end-start)

# Timer Function for average running time [6]


def ave_runtime(num_runs, size, sort_algo):
    # Empty array to store results
    trial_dict_times = []
    # While loop that runs the algorithm a set  number of times
    counter = 0
    while counter < num_runs:
        input_array = array_test(size)
        trial_dict_times.append(timer(input_array, sort_algo))
        counter = counter + 1
    # return average runtime of the algorithm
    return (sum(trial_dict_times)/len(trial_dict_times))

# Section 4 - Formatting the output

# create a function to carry out the trial_dicts [7]


def algo_trial_dict(algo, test_size):
    # Get the averge run time of an algoritm and test size that is ran 10 times
    return float("{:10.3f}".format(ave_runtime(10, test_size, algo)*1000))

# Function to create col
# Algo and test size passed in as arguments


def col_create(algos, test_size):
    # For loop tests each algorithm for the test size
    col = []
    for i in algos:
        col.append(algo_trial_dict(i, test_size))
    # return results
    return(col)

# Create DataFrame function and pass a dict to the function


def DF_Data(data_dict):
    # Create the DF and select the index to be the the size field
    data = pd.DataFrame(data_dict)
    data.set_index("size", inplace=True)
    # Retrun the data
    return data


# Funcation that plots the results based of the dictionary
# Arguments sort algo and test size are passed to the function
def results_plot(data_dict, test_size, sort_algos):
    # create a PANDAS DF with data_dict
    data = DF_Data(data_dict)
    # loop through the list
    for i in range(len(five_algo)):
        plt.plot(test_size, data.iloc[i], label=sort_algos[i])
    # Plot and show the graph x+y axis, title & legend
    plt.xlabel("Input Size, n")
    plt.ylabel("Run Time Average, ms")
    plt.title("Sorting actual_algoname")
    plt.legend()
    plt.show()


# create a list of  sorting actual_algoname
# "five_algo" to be used as an index for the data frame
five_algo = ['Bubble Sort', 'Insertion Sort',
             'Selection Sort', 'Merge Sort', 'Counting Sort']
# "actual_algoname" is a list of the function names
actual_algoname = [bubbleSort, insertionSort, selectionSort,
                   mergeSort, countingSort]
# n_trial_dictsizesize is a list of input sizes to be tested as per the question
n_trial_dictsize = [100, 250, 500, 750, 1000, 1250,
                    2500, 3750, 5000, 6250, 7500, 8750, 10000]
# trial_dict is a data dictionary used to create the columns for the PANDAS DF
trial_dict = {"size": five_algo, "100": col_create(actual_algoname, 100), "250": col_create(actual_algoname, 250), "500": col_create(actual_algoname, 500), "750": col_create(actual_algoname, 750), "1000": col_create(actual_algoname, 1000), "1250": col_create(actual_algoname, 1250), "2500": col_create(
    actual_algoname, 2500), "3750": col_create(actual_algoname, 3750), "5000": col_create(actual_algoname, 5000), "6250": col_create(actual_algoname, 6250), "7500": col_create(actual_algoname, 7500), "8750": col_create(actual_algoname, 8750), "10000": col_create(actual_algoname, 10000)}

# Main user function to navigate data


def main():
    # user interface with three options
    choices = ["graph", "table", "quit"]
    choice_selected = input(
        "Please select a viewing choice - graph/table/quit   ")
    # While loop to validates input
    while choice_selected not in choices:
        choice_selected = input(
            "Please select a viewing choice - graph/table/quit  ")
    # use a conditional statements to control the flow
    # function doesnt end until user quits
    if choice_selected == "graph":
        results_plot(trial_dict, n_trial_dictsize, five_algo)
        main()
    elif choice_selected == "table":
        print(DF_Data(trial_dict).to_string())
        main()
    else:
        quit()


print()
main()


# References
# [1] https://www.studytonight.com/data-structures/bubble-sort
# [2] http://www.openbookproject.net/books/pythonds/five_algoearch/TheMergeSort.html
# [3] https://runestone.academy/runestone/books/published/pythonds/five_algoearch/TheSelectionSort.html
# [4] https://www.freecodecamp.org/news/sorting-algorithm-explained-with-examples-in-python-java-and-c/
# [5] https://www.happycoders.eu/algorithm/counting-sort/
# [6] https://docs.python.org/3/library/time.html
# [7] https://thepythonguru.com/python-string-formatting/
# [8] https://docs.python.org/3/library/random.html
