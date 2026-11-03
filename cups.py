#!/usr/bin/env python3

import sys

from priority_queue import PriorityQueue

# Functions

def fill_cups(cups):
    # TODO
    #add the cup counts first to pq
    pq = PriorityQueue(cups)
    secs = 0
    while (pq.peek() > 0):
        a = pq.pop()
        b = pq.pop()
        a -= 1
        if b > 0:
            b -= 1
        pq.push(b)
        pq.push(a)
        secs += 1
    return secs

def main(stream=sys.stdin):
    # TODO
    for line in stream:
        cups = list(map(int, line.split()))
        print(fill_cups(cups))

if __name__ == '__main__':
    main()
