'''
2018/05/10 potter select_sort
'''
import numpy as np         
import random 

def swap(a,b,plist):
    temp = plist[a]
    plist[a] = plist[b]
    plist[b] = temp

def Select_Sort(num_list):
    i=0
    for i in range(len(num_list)-1):
        for j in  range(i+1,len(num_list)):
            if num_list[j]<num_list[i]:
                swap(i,j,num_list)
    return num_list


if __name__=='__main__':
    num = int(input('please input a number:'))
    num_list = [x for x in range(num)]
    random.shuffle(num_list)
    print('num_list:',num_list)
    result = Select_Sort(num_list)
    print('result:  ',result)
