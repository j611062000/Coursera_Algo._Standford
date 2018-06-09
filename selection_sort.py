def selection_sort(array):

    start = 0

    while True:

        # to catch the index of minimum value in a subarray
        index = start
        # to catch the minimum value in a subarray
        min_temp = array[start]

        for i in range(start, len(array)):

            if array[i] < min_temp:
                min_temp = array[i]
                index = i
        # moving the minimum value to the first place in a subarray
        temp = array[index]
        del array[index]
        array.insert(start,temp)

        if start+1 == len(array):
            break
        else:
            start+=1

    return array

print(selection_sort([1,4,2,100,3,1,-1]))
