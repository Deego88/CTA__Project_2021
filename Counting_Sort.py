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


sortedList = countingSort([22, 55, 91, 15, 66, 22, 25, 5, 18])
print(sortedList)
