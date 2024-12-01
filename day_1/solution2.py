#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

def main():
    
    file = pd.read_csv('input.txt', sep='   ', names=['list1','list2'])
    list1 = file['list1'].copy()
    list2 = file['list2'].copy()
    merged = pd.merge(left=pd.Series(list1.unique(), name='list1'),
                   right=list2.value_counts().reset_index(),
                   left_on='list1',
                   right_on='list2',
                   how='inner')
    print(sum([x['list1'] * x['count'] for _, x in merged.iterrows()]))

if __name__ == "__main__":
    main()
