#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

def main():
    
    file = pd.read_csv('input.txt', sep='   ', names=['list1','list2'])
    list1 = file['list1'].copy()
    list2 = file['list2'].copy()
    list1.sort_values(inplace=True)
    list2.sort_values(inplace=True)
    length = len(list1)
    print(sum([abs(list1.iloc[x] - list2.iloc[x]) for x in range(length)]))

if __name__ == "__main__":
    main()
