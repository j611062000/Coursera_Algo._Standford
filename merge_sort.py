def isIndexSafe(index, array):
    """
    Check if the index is in the range of array
    """
    if index <= len(array)-1:
        return True
    elif index > len(array)-1:
        return False

def mergesort(array):

    if len(array) <= 1:
        return array

    l=len(array)//2
    Larray=mergesort(array[:l])
    Rarray=mergesort(array[l:])

    temp=[]
    i=-1
    j=-1

    while isIndexSafe(i+1,Larray) or isIndexSafe(j+1,Rarray):

        if isIndexSafe(i+1,Larray) and isIndexSafe(j+1,Rarray):
            if Larray[i+1]>Rarray[j+1]:
                temp.append(Rarray[j+1])
                j+=1
            else:
                temp.append(Larray[i+1])
                i+=1

        elif isIndexSafe(i+1,Larray):
            temp.append(Larray[i+1])
            i+=1

        elif isIndexSafe(j+1,Rarray):
            temp.append(Rarray[j+1])
            j+=1

    return temp

print(mergesort([5,1,0,4,6,8,7]))


