

import copy

def combine(array,comb_num):
    length = len(array)
    result = []
    item = [0]*comb_num
    def next_item_item(loop_num=0,num=0):
        if num == comb_num:
            result.append(copy.copy(item))
            return
        for i in range(loop_num,length):
            item[num]=array[i]
            next_item_item(i+1,num+1)

    next_item_item()
    return result
arrayList = [1, 2, 3, 4, 5]
for i in range(len(arrayList)+1):
    print(combine(arrayList,i))