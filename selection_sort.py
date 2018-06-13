def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

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
        swap(array, index, start)

        if start+1 == len(array):
            break
        else:
            start+=1
        print(array)
    return array

if __name__ == "__main__":
    print(selection_sort([1,100,2,42,2,1,33]))
