class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        for a given endpoint, look at the most recent endpoint. if smaller, skip over
        since the recent endpoint covers it. if larger, start a new interval
        """
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
        return res

        