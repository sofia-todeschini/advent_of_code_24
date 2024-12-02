#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def check_safety(alist):

    if(alist[1] - alist[0]) > 0:
        is_increasing=True
    else:
        is_increasing=False

    for i in range(1,len(alist)):
        if abs(alist[i-1] - alist[i]) == 0:
            return False
        if abs(alist[i-1] - alist[i]) > 3:
            return False
        
        if is_increasing and alist[i] - alist[i-1] < 0:
            return False
        
        if not is_increasing and alist[i] - alist[i-1] > 0:
            return False
        
    return True


def recheck_safety(alist):

    print(alist)
    for i in range(len(alist)):
        new_list = [alist[j] for j in range(len(alist)) if i != j]
        print(new_list)

        if check_safety(new_list):
            return True
    
    return False
    

def main():
    
    with open('day_2/input.txt', 'r') as f:
        data = [x[:-1].split(' ') for x in f.readlines()]
    
    data_int = []

    for i in range(len(data)):
        data_int.append([])
        for elem in data[i]:
            data_int[i].append(int(elem))
    
    safe_count = 0

    for elem in data_int:
        if check_safety(elem):
            safe_count+=1
        
        elif recheck_safety(elem):
            safe_count+=1
    
    print(safe_count)

    

if __name__ == "__main__":
    main()
