class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs_mark(i, j, grid):
            if 0 <= i < len(grid) and 0<= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0' # 注意，是字符串'0'和'1'。而不是int。int 0才是False呢！
                # 以i j坐标为起点，在进行DFS。所以，在下一层才需要判断碰壁不。而在这一层不需要。
                dfs_mark(i-1, j, grid)
                dfs_mark(i+1, j, grid)
                dfs_mark(i, j-1, grid)
                dfs_mark(i, j+1, grid)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    dfs_mark(i, j, grid)
        return count
        

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def bfs_mark(i, j, grid):
            queue = [(i, j)]
            while queue:
                i, j = queue.pop(0) # 这句可是在if外面的哦。
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue.extend([(i-1, j), (i+1, j), (i, j-1), (i, j+1), ])
                

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    bfs_mark(i, j, grid)
        return count