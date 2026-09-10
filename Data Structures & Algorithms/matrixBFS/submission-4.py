from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        start = (0,0)
        end = (len(grid)-1, len(grid[0])-1)

        rows = len(grid)
        cols = len(grid[0])

        queue = deque([start])
        visited = {start}

        directions = {(-1, 0), (1, 0), (0,-1), (0,1) }

        distance = 0

        if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
            return -1

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                

                if (r, c) == end:
                    return distance
                
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] != 1
                        and (nr, nc) not in visited
                    ):

                        visited.add((nr,nc))
                        queue.append((nr,nc))
                        
            distance +=1
            
        return -1


