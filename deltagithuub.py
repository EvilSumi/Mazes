from pyamaze import maze,agent


m=maze(15,20) 
#m.CreateMaze( #pattern='h/v'  #saveMaze=True #loopPercent=40 #loadmaze='text.csv')
m.CreateMaze(loopPercent=40)

m.run()