def quickSort(array, leftIndex, rightIndex):
    if leftIndex < rightIndex:
        pivot_index = partition(array, leftIndex, rightIndex)
        quickSort(array, leftIndex, pivot_index - 1)
        quickSort(array, pivot_index + 1, rightIndex)


def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]


def partition(array, leftIndex, rightIndex):
    pivot_index = leftIndex
    pivot_value = array[pivot_index]
    left_index = pivot_index + 1
    right_index = rightIndex

    while True:  # if left_index is at the right-hand side of right_index, breaking while
        while array[left_index] <= pivot_value and left_index < rightIndex:
            left_index += 1
        while array[right_index] > pivot_value and right_index > pivot_index:
            right_index -= 1
        if left_index < right_index:
            swap(array, left_index, right_index)
        if left_index >= right_index:
            break

    swap(array, right_index, pivot_index)
    return right_index


def partitionTest():
    input_data = [[5, 1, 3, 8, 9], [5, 8, 3, 1, 9, 3],
                  [1, 2, 3, 4], [3, 1], [4, 3, 2, 1], [1, 3]]
    for test in input_data:
        pivot_index = partition(test, 0, len(test) - 1)
        print("pivot_index=%s, test=%s" % (pivot_index, test))


def quicksorTest():
    input_data = [[3, 4],
                  [5, 1, 3, 8, 9],
                  [5, 8, 3, 1, 9, 3],
                  [1, 2, 3, 4],
                  [1,3],
                  [4,3,2,1],
                  [3,1]
                 ]
    for test in input_data:
        quickSort(test, 0, len(test) - 1)
        correct_ans = sorted(test)
        print("isTestCorrect=%s" % ((test == correct_ans)))

if __name__ == "__main__":
    test = 1
    if test == 1:
        quicksorTest()
    else:
        partitionTest()
