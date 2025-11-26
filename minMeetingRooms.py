# 253. Meeting Rooms II

#Definition of Interval:
from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        count, output = 0, 0
        s, e = 0, 0
        
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            output = max(output, count)
        return output
        
if __name__ == "__main__":
    sol = Solution()
    intervals = [Interval(0, 40), Interval(5, 10), Interval(15, 20)]
    print("Output is:", sol.minMeetingRooms(intervals))  # Expected False [web:2][web:4][web:6]
