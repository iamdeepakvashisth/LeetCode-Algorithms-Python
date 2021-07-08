'''
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

 
'''

def isPathCrossing(self, path: str) -> bool:
        s = [(0,0)]
        i,j=0,0
        for p in path:
            if p == "N":
                j += 1
                if (i,j) not in s:
                    s.append((i,j))
                else:
                    return True
            elif p == "E":
                i += 1
                if (i,j) not in s:
                    s.append((i,j))
                else:
                    return True
            elif p == "S":
                j -= 1
                if (i,j) not in s:
                    s.append((i,j))
                else:
                    return True
            else:
                i -= 1
                if (i,j) not in s:
                    s.append((i,j))
                else:
                    return True
        return False
        