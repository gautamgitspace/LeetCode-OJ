#!/usr/bin/env python3

def split_point(arr, n):
    leftsum = 0
    rightsum = 0
    for i in range(0, n):
        leftsum += arr[i]

    for i in range(n-1, -1, -1):
        rightsum += arr[i]
        print ("rightsum is: " + str(rightsum))

        leftsum -= arr[i]
        print ("leftsum is: " + str(leftsum))

        if rightsum == leftsum:
            return i

    return -1

def split_array(arr, n):
    split_idx = split_point(arr, n)

    if split_idx == -1 or split_idx == n:
        print ("can't be done")
    left_array = []
    right_array = []
    for i in range(0, split_idx):
        left_array.append(arr[i])
    for i in range(n-1, split_idx-1, -1):
        right_array.append(arr[i])

    print (left_array)
    print (right_array)
    print ("split_idx: " + str(split_idx))


# DRIVER
base_array = [1,2,3,4,5,5]
split_array(base_array, len(base_array))
