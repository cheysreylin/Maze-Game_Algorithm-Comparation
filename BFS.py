from timeit import timeit
from pyamaze import maze,agent,COLOR,textLabel

def BFS(m):
    start=(m.rows,m.cols) # last row, last column
    visiting_node =[start]
    visited_node =[start]

    bfsPath={}
    while len(visiting_node)>0:
        current_cell=visiting_node.pop(0)
        if current_cell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[current_cell][d]==True:
                if d=='E':
                    neighbor_Cell = (current_cell[0],current_cell[1]+1)
                elif d=='W':
                    neighbor_Cell = (current_cell[0],current_cell[1]-1)
                elif d=='N':
                    neighbor_Cell = (current_cell[0]-1,current_cell[1])
                elif d=='S':
                    neighbor_Cell = (current_cell[0]+1,current_cell[1])
                    
                if neighbor_Cell in visited_node:
                    continue

                visiting_node.append(neighbor_Cell)
                visited_node.append(neighbor_Cell)
                bfsPath[neighbor_Cell] = current_cell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return fwdPath

if __name__=='__main__':
    m=maze(10,10)
    m.CreateMaze(loopPercent=10)
    path=BFS(m)

    a=agent(m,footprints=True,filled=True, color = COLOR.red)
    m.tracePath({a:path})
    l=textLabel(m,'Length of Shortest Path',len(path)+1)
    time = timeit(number=1000, globals= globals())
    textLabel(m, "Timer: ", time)

    m.run()
    m.run()