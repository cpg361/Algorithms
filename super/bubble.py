'''
2018/05/14 super bubble
'''
#import numpy as np         
import random

def bubble(num_list):
    len_list = len(num_list)
    for i in range(len_list - 1):
        for j in range(len_list - i - 1):
            if num_list[j] > num_list[j + 1]:
                tmp = num_list[j]
                num_list[j] = num_list[j + 1]
                num_list[j + 1] = tmp
    return num_list

if __name__ == '__main__':
    num = int(input('please input a number:'))
    num_list = [x for x in range(num)]
    random.shuffle(num_list)
    print('num_list:', num_list)
    result = bubble(num_list)
    print('result:', result)
