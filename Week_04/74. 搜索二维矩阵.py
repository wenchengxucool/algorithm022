class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        left, right, mid = 0, len(matrix) - 1, 0
        while left <= right:
            mid = left + (right - left) / 2            
            if matrix[mid][0] == target or target == matrix[mid][-1]:
                return True
            if matrix[mid][0] < target < matrix[mid][-1]:
                break
            elif matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][-1] < target:
                left = mid + 1
        
        left, right = 0, len(matrix[mid]) - 1
        while left <= right:
            mid_ = left + (right - left) / 2            
            if matrix[mid][mid_] == target:
                return True
            elif matrix[mid][mid_] > target:
                right = mid_ - 1
            elif matrix[mid][mid_] < target:
                left = mid_ + 1
        
        return False