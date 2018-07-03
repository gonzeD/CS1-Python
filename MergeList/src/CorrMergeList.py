#!/usr/bin/python3
# -*- coding: utf-8 -*-

def merge(first_list, second_list):
    list = []
    i,j = 0,0
    max1,max2 = len(first_list),len(second_list)
    while (i< max1 and j < max2):
        if (first_list[i][1] < second_list[j][1]):
            list.append(first_list[i])
            i+=1
        else:
            list.append(second_list[j])
            j+=1
    if i< max1:
        list.extend(first_list[i:])
    if j< max2:
        list.extend(second_list[j:])
    return list   