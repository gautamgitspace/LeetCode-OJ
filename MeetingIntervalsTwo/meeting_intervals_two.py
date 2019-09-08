#!/usr/bin/env python3

import heapq

def rooms_required(intervals):
    start = []
    end = []
    for s, e in intervals:
        start.append(s)
        end.append(e)

    start.sort()
    end.sort()

    sp, ep = 0, 0
    min_rooms, count_rooms = 0, 0
    while sp < len(start):
        if start[sp] < end[ep]:
            count_rooms += 1
            min_rooms = max(min_rooms, count_rooms)
            sp += 1
        else:
            count_rooms -= 1
            ep += 1
    return min_rooms


if __name__ == "__main__":
    intervals = [[5,60], [0,50], [15,20], [30,45]]
    print(rooms_required(intervals))
