class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        finalInterval = []
        last_appended_interval = None
        for interval in intervals:
            if last_appended_interval and interval[0] < last_appended_interval[1] < interval[1]:
                last_appended_interval = [min(last_appended_interval[0],interval[0]) , max(interval[1], last_appended_interval[1])]
                finalInterval[-1] = last_appended_interval
                continue
            if interval[0] > newInterval[1]:
                finalInterval.append(newInterval)
                last_appended_interval = interval
                # finalInterval.append(interval)
            elif interval[0] < newInterval[0] < interval[1]:
                newInterval = [interval[0], max(newInterval[1], interval[1])]
                last_appended_interval = newInterval
                # finalInterval.append(newInterval)
            elif interval[1] < newInterval[0] :
                last_appended_interval = interval
                # finalInterval.append(interval)
            finalInterval.append(last_appended_interval)
        return finalInterval