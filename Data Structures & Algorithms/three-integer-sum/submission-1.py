from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Sort the array to easily handle duplicates and use pointers
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n):
            # Optimization: If the current number is greater than 0, 
            # it's impossible for any subsequent numbers to sum up to 0
            if nums[i] > 0:
                break
                
            # Skip duplicate values for the first element of the triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Step 2: Initialize two pointers for the remaining subarray
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move pointers inward and skip duplicates to avoid identical triplets
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif current_sum < 0:
                    # Sum is too small; move the left pointer to increase the sum
                    left += 1
                else:
                    # Sum is too large; move the right pointer to decrease the sum
                    right -= 1
                    
        return result
