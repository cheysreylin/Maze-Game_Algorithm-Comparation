# from BFS import BFS
# from A_star import aStart_search
# from pyamaze import maze, agent, COLOR, textLabel
# from timeit import timeit

# # mMaze = maze(20,30)
# # mMaze.CreateMaze(loopPercent=100,theme= 'light')
# mMaze = maze()
# mMaze.CreateMaze(loadMaze='maze--2022-07-15--15-39-56.csv')
# visiting_node,fwdpath,bfsPath = BFS(mMaze)
# asearchPath,aPath,fwdaPath = aStart_search(mMaze)

# t1 = textLabel (mMaze, 'A* Path Length',len(fwdaPath)+1)
# t2 = textLabel (mMaze, 'BFS Path Lenght', len (fwdpath)+1)
# t3 = textLabel (mMaze, 'A* Search', len(asearchPath)+1)
# t4 = textLabel (mMaze, 'BFS Search',len(visiting_node)+1)

# a = agent (mMaze, footprints=True, color=COLOR.cyan, filled = True)
# b = agent (mMaze, footprints=True, color=COLOR.yellow)
# # c = agent (mMaze,1,1, footprints=True, color=COLOR.green,shape = 'square', filled= True, goal=(mMaze.rows, mMaze.cols))
# mMaze.tracePath({a:fwdpath},delay = 100)
# mMaze.tracePath({b:fwdaPath},delay = 100)
# # mMaze.tracePath({c:asearchPath}, delay = 100)
# time1 = timeit(stmt='aStar (mMaze)', number=1000,globals=globals())
# time2 = timeit(stmt='bfs (mMaze)', number=1000,globals=globals())

# textLabel(mMaze,'A-Star Time',time1)
# textLabel(mMaze,'BFS Time', time2)


# mMaze.run()
