def isIndexSafe(index, array): #Check if the index is in the range of array

    if index <= len(array)-1:
        return True
    elif index > len(array)-1:
        return False

def inversionCountByMergesort(array):

    global inversion_count # record the number of inversion in this subarray

    if len(array) == 1:
        return array

    l=len(array)//2  # divide the original problem to subproblems by recurssion
    Larray = inversionCountByMergesort(array[:l])
    Rarray = inversionCountByMergesort(array[l:])

    temp = []        # merge the solution of these 2 subproblems to get the global solution
    l_index = 0
    r_index = 0

    for i in range(len(array)):

        if isIndexSafe(l_index, Larray) and isIndexSafe(r_index, Rarray):

            if Larray[l_index] > Rarray[r_index]:
                temp.append(Rarray[r_index])
                r_index+= 1
                inversion_count+=len(Larray) - l_index
            else:
                temp.append(Larray[l_index])
                l_index+= 1

        elif isIndexSafe(l_index, Larray):
            temp+=Larray[l_index:]
            break

        else:
            temp+=Rarray[r_index:]
            break
    return temp

# test case listed as below

global inversion_count
inversion_count = 0

temp = []
with open("apple.txt", "r") as file:
    for element in file.readlines():
        temp.append(int(element[:-1]))
inversionCountByMergesort( temp)
print(inversion_count)
