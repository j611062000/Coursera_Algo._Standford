from math import sqrt
from matplotlib.pyplot import plot, axis, show

def distanceOf2Pairs(p1,p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def bruteForceDistance(point_set):
    distance_temp = float("inf")

    for i in range(len(point_set)):
        for j in range(i+1,len(point_set)):
            if distanceOf2Pairs(point_set[i], point_set[j]) < distance_temp:
                distance_temp = distanceOf2Pairs(point_set[i], point_set[j])
    return distance_temp

def isPeerInRectangle(left_point, right_point, delta):
    if right_point[1] < left_point[1] + delta and \
       right_point[1] > left_point[1] - delta:
        return True
    else:
        return False

def construcStrip(sortedDataByX, delta):
    pivot   = (len(sortedDataByX) // 2) - 1
    pivot_x = sortedDataByX[pivot][0]
    i       = pivot + 1
    right_strip = []
    left_strip  = [sortedDataByX[pivot]]

    while True:
        if sortedDataByX[i][0] - pivot_x <= delta:
            right_strip.append(sortedDataByX[i])
            i+=1
            if i >= len(sortedDataByX):
                break
        else:
            break

    i = pivot - 1
    while True:
        if pivot_x - sortedDataByX[i][0] <= delta:
            left_strip.append(sortedDataByX[i])
            i-=1
            print()
            if i < 0:
                break
        else:
            break
    return [left_strip, right_strip]

def divideAndConquerDistance(point_set):

    if len(point_set) <= 3:
        return bruteForceDistance(point_set)

    sorted(point_set, key = lambda pair: pair[0]) # sorting the data by x-coordinate
    dividing_point     = len(point_set) // 2
    left_min_distance  = divideAndConquerDistance(point_set[:dividing_point])
    right_min_distance = divideAndConquerDistance(point_set[dividing_point:])
    delta              = min(left_min_distance, right_min_distance)

    left_strip, right_strip = construcStrip(point_set, delta)
    sorted(right_strip, key = lambda pair: pair[1])
    min_split_distance = delta

    for element in left_strip:
        for peer in right_strip:
            if isPeerInRectangle(element, peer, delta) and \
               distanceOf2Pairs(element, peer) < min_split_distance:
                   min_split_distance = distanceOf2Pairs(element, peer)

    return min(min_split_distance, left_min_distance, right_min_distance)

if __name__ == "__main__":

    data = [(3.8,4.5),(3,4),(-1,5),(0,-9),(5,5),(2,19),(-8,-8),(7,1),(1,1),(1,1)]
    print(divideAndConquerDistance(data))
    print(bruteForceDistance(data))
    plot([pair[0] for pair in data],[pair[1] for pair in data],"bo")
    show()

