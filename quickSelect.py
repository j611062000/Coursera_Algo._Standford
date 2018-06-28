def quickSelect(array, left, right, Kth):
    if left == right:
        return array[left]

    else:
        pivotIndex = left
        pivotIndex = partition(array, left, right, pivotIndex)

        if Kth - 1 == pivotIndex:
            return array[pivotIndex]

        elif Kth - 1 < pivotIndex:
            return quickSelect(array, left, pivotIndex - 1, Kth)

        else:
            return quickSelect(array, pivotIndex + 1, right, Kth)


def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]


def partition(array, left, right, pivotIndex):
    pivot_value = array[pivotIndex]
    swap(array, pivotIndex, right)
    temp_index = left

    for i in range(left, right):
        if array[i] <= pivot_value:
            swap(array, i, temp_index)
            temp_index += 1
    swap(array, temp_index, right)
    return temp_index


def test_partition():
    dataset = [
        [2, 4, 5, 1],
        [2, 7, 4, 1],
        [9, 4, 333, 1],
        [1, 2, 3],
        [5, 3, 2],
        [1, 2],
        [2, 1]
    ]
    for data in dataset:
        print(partition(data, 0, len(data) - 1, 0))


def test_quickSelect():
    datasets = [[1,2,5,3,4],[1,2],[2,1]]
    for dataset in datasets:
        temp_data = dataset
        for i in range(len(dataset)):
            dataset = temp_data
            print(quickSelect(dataset, 0, len(dataset)-1, i + 1))
        print("end of this test case")


if __name__ == "__main__":
    test_quickSelect()
