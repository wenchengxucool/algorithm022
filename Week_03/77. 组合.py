class Solution(object):
    def combine(self, n, k):
        """k得用啊！"""
        ans = []
        def dfs(alist, idx):
            if idx == k: # 确定是n。因为下面range(idx+1, n+1)。当idx==n时，为空。
                ans.append(alist)
                return
            for i in range(1+idx, 1+n):
                if len(alist) == 0 or (len(alist) > 0 and alist[-1] < i):
                    dfs(alist + [i], idx+1) 
        dfs([], 0)
        return ans