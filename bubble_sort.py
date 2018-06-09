def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

def bubble_sort(array):
    """
    if the len(array) is n, then it takes n-1 steps to finish the bubble sort
    """
    swap_count = 1

    """
    when there is a while loop whithout any swap, the array has been sorted thoroughly
    """
    while swap_count > 0:
        swap_count = 0
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                swap(array, i, i+1)
                swap_count+=1

    return array

print(bubble_sort([5,1,4,6,7,8,10,1,2,3]))

