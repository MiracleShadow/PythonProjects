'''
将所有的数据建成一个堆，最大的数据在堆顶，然后将堆顶的数据元素和序列的最后一个元素交换
接着重建堆、交换数据，一次下去，从而实现对所有的数据元素的排序
完成堆排序所需要执行的两个动作：建堆、堆的调整（反复进行）
'''

#获取左右叶子节点
def LEET(i):
    return 2*i+1

def RIGHT(i):
    return 2*i+2

############调整大顶堆############
#data_list:待调整序列  length:序列长度  i:需要调整的结点
def adjust_max_heap(data_list,length,i):
    #定义一个int值保存当前序列最大值的下标
    largest = i
    #执行循环操作：1、寻找最大值的下标 2、最大值与父结点交换
    while 1:
        left,right = LEET(i),RIGHT(i)
        if (left<length)and(data_list[left]>data_list[i]):
            largest=left
        if (right<length)and(data_list[right]>data_list[largest]):
            largest=right
        if (largest!=i):
            data_list[i],data_list[largest]=data_list[largest],data_list[i]
            i=largest
            #print(largest)
            continue
        else:
            break

############建立大顶堆############
def build_max_heap(data_list):
    length=len(data_list)
    for x in range(int((length-1)/2),-1,-1):
        adjust_max_heap(data_list,length,x)


def heap_sort(data_list):
    build_max_heap(data_list)
    i=len(data_list)
    while i>0:
        print(data_list)
        data_list[0],data_list[i-1]=data_list[i-1],data_list[0]
        i=i-1
        adjust_max_heap(data_list,i,0)

a=[7,4,1,8,5,2,9,6,3]
heap_sort(a)