# -*- coding: utf-8 -*-
import random

#直接插入排序

def insert_sort(array):

    size = len(array)
    for i in range(1,size):
        num = array[i]
        j = i - 1
        while j>=0:
            if array[j]>num:
                array[j + 1]=array[j]
                array[j]=num
            j -= 1
    return array
#方式二
def insertSort(array):
    length = len(array)
    for i in range(length):
        for j in range(i):
            if array[i]<array[j]:
                array.insert(j,array[i])
                array.pop(i+1)
    return array

#二分查找
def mid_search(array, item):
    low = 0
    high = len(array) - 1
    while low<=high:
        mid = int((low+high)/2)
        guess = array[mid]
        if guess>item:
            high = mid -1
        elif guess<item:
            low = mid +1
        else:
            return mid
    return None

#冒泡排序
def bubbleSort(array):
    length = len(array)
    for i in range(length):
        for j in range(length-i-1):
            if array[j]>array[j+1]:
                array[j], array[j + 1]= array[j + 1], array[j]
    return array
#选择排序
def selectSort(array):
    length = len(array)
    for i in range(length):
        for j in range(i+1,length):
            if array[i]>array[j]:
                array[i], array[j] = array[j], array[i]
    return array

#快速排序
def quickSort(array):
    if len(array)<2:
        return array
    else:
        pivot = array[0]
        lessarray = [i for i in array[1:] if i<=pivot]
        morearray = [i for i in array[1:] if i>pivot]
        return quickSort(lessarray)+[pivot]+quickSort(morearray)

#希尔排序
def shell_insert(array):
    length = len(array)
    gap = int(length/2)
    while gap > 0:
        for i in range(gap,length):
            temp = array[i]
            j = i
            while j>=gap and array[j-gap]>temp:
                array[j]=array[j-gap]
                j-=gap
            array[j]=temp
        gap = int(gap/2)
    return array

#归并排序
def merge(left,right):
    result = []
    while left and right:
        result.append(left.pop(0) if left[0]<=right[0] else right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result
def mergeSort(array):
    if len(array)==1:
        return  array
    mid = int(len(array)/2)
    left = mergeSort(array[:mid])
    right  = mergeSort(array[mid:])
    return merge(left,right)

def main():
    randomList = [random.randint(1,100) for i in range(10)]
    print(insert_sort(randomList))
    randomList = [random.randint(1, 100) for i in range(10)]
    print(insertSort(randomList))
    randomList = [random.randint(1, 100) for i in range(10)]
    print(bubbleSort(randomList))
    randomList = [random.randint(1, 100) for i in range(10)]
    print(selectSort(randomList))
    randomList = [random.randint(1, 100) for i in range(10)]
    print(quickSort(randomList))
    randomList = [random.randint(1, 100) for i in range(10)]
    print(shell_insert(randomList))
    randomList = [random.randint(1, 100) for i in range(10)]
    print(mergeSort(randomList))
    mid_list = [1,3,5,10,34,99]
    print(mid_search(mid_list,34))
    print(type((1)))
main()


