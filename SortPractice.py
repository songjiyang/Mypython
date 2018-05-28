# -*- coding: utf-8 -*-
import random

#插入排序

def insert_sort(lists):

    size = len(lists)
    for i in range(1,size):
        num = lists[i]
        j = i - 1
        while j>=0:
            if lists[j]>num:
                lists[j+1]=lists[j]
                lists[j]=num
            j -= 1
    return lists


def main():
    print(insert_sort([random.randint(1,100) for i in range(10)]))


main()