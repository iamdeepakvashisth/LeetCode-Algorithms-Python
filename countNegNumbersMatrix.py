'''
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
'''
def countNegatives(self, grid: List[List[int]]) -> int:
    count=0
    for i in grid:
        for j in i:
            if j<0:
                count+=1
    return count