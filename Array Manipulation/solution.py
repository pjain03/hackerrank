#!/bin/python3

import sys

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    # val has n + 1 keys
    val = [0 for _ in range(n + 1)]
    for a0 in range(m):
        a, b, k = input().strip().split(' ')
        # we stagger the starting and ending positions because we add k at a and subtract it at b. Since we want
        # to "include" both a and b, we need to stagger the values stored which is why val has n + 1 keys as well.
        val[int(a) - 1] += int(k)
        val[int(b)] -= int(k)
        
    maxk = 0
    currk = 0
    visited = []
    # go through number line
    for item in val:
        currk = currk + item
        # update max k value seen    
        if currk > maxk:
            maxk = currk
    print(maxk)        
    # this implementation runs in O(n + m) time
        