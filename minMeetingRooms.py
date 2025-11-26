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
