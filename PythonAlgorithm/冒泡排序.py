#coding=utf-8
def bubble_sort (list):
    length=len(list)
    for index in range(length):
        for i in range(1,length-index):
            if list[i-1]<list[i]:
                list[i],list[i-1]=list[i-1],list[i]
    return list
list=[10,23,1,53,654,54,16,646,65,3155,546,31]
print( bubble_sort(list))