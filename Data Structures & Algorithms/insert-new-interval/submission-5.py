class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        finalInterval =[]
        
        if intervals[0][0] >  newInterval[1]:
            return [ newInterval, *intervals ]
        elif intervals[-1][1] < newInterval[0]:
            return [*intervals, newInterval ]
        else:
            i = 0
            # final_list = []
            
            while i < (len(intervals)-1):
                # i [0][1]  i+1 [0][1]
                if intervals[i][0] < newInterval[0] and newInterval[1] < intervals[i+1][1]:
                    # i[0][1], new[0][1], i+1[0][1]
                    if intervals[i][1] < newInterval[0] and newInterval[1] < intervals[i+1][0]:
                        return [*intervals[:i + 1], newInterval, *intervals[i + 1:]]
                        # final_list.append(newInterval)
                    # i[0], i+1[1]
                    elif intervals[i][0] < newInterval[0] < intervals[i][1] < intervals[i+1][0] < newInterval[1] < intervals[i+1][1]:
                        mergedInterval = [intervals[i][0], intervals[i+1][1]]
                        return [*intervals[:i], mergedInterval, *intervals[i + 2:]]
                    # i[0], new[1]
                    elif intervals[i][0] < newInterval[0] < intervals[i][1] < newInterval[1]:
                        mergedInterval = [intervals[i][0], newinterval[1]]
                        return [*intervals[:i], mergedInterval, *intervals[i + 1:]]
                    elif newinterval[0] < intervals[i+1][0] < newinterval[1] < intervals[i+1][1]:
                        mergedInterval = [newinterval[0], intervals[i+1][1]]
                        return [*intervals[:i+1], mergedInterval, *intervals[i + 2:]]

                i = i + 1
                # final_list.append(newInterval)
            
            return intervals


        