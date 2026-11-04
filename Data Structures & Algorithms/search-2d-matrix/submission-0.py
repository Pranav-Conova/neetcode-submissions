class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left, right, inner_length = 0, len(matrix) - 1, len(matrix[0]) -1
        if target < matrix[0][0] or target > matrix[right][inner_length] :
            
            return False
        while left <= right:
            mid = left + (right - left) // 2
            print(matrix[mid])
            if matrix[mid][0] < target < matrix[mid][inner_length]:
                left = mid
                break
            elif matrix[mid][inner_length] < target:
                left = mid + 1
            else:
                right = mid - 1
        print(left)
        final_matrix = matrix[left]
        print(final_matrix)
        left, right = 0, len(final_matrix) -1
        while left <= right:
            mid = left + (right - left) // 2
            if final_matrix[mid] == target:
                return True
            elif final_matrix[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False