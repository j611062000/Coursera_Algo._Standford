from bisect import bisect_left, bisect_right

def twoSum(filename, target_range=(-10000,10000)):
    with open(filename, 'r') as file:
        input_data = [int(line.rstrip()) for line in file]
    input_data.sort()

    result = set([])

    for num1 in input_data:
        lb = bisect_left(input_data, target_range[0] - num1)
        ub = bisect_right(input_data, target_range[1] - num1)
        for num2 in input_data[lb:ub]:
            result.add(num1 + num2)

    return len(result)


if __name__ == '__main__':
    result = twoSum('twoSumData.txt')
    print (result)

#427
