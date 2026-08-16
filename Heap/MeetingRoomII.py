'''
253. Meeting Rooms II

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])

        heap = []

        for start, end in intervals:

            if heap and start >= heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, end)

        return len(heap)