class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        used = {x:False for x in nums}
        def dfs(temp, depth, nums, used):
            if depth == len(nums):
                ans.append(temp)
                return
            for n in nums:
                if not used[n]:
                    used[n] = True
                    dfs(temp+[n], depth+1, nums, used)
                    used[n] = False
        dfs([], 0, nums, used)
        return ans