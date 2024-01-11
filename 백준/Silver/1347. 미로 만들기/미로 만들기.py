import sys
input = sys.stdin.readline

N = int(input())
dy = [-1,0,1,0]
dx = [0,-1,0,1]
maze_way = list(input())
direction_index = 0
now_position = [0,0]
way_point = [[0,0]]

for i in range(len(maze_way)):
    if maze_way[i] == "R":
        direction_index = (direction_index + 1) % 4
    if maze_way[i] == "L": 
        direction_index = (direction_index - 1) % 4
    if maze_way[i] == "F":
        now_position[0] += dy[direction_index]
        now_position[1] += dx[direction_index]
        # print(now_position.copy())
        way_point.append(now_position.copy())
max_y,min_y,max_x,min_x = -100,100,-100,100
for y,x in way_point:
    if max_y < y : max_y = y
    if min_y > y : min_y = y
    if max_x < x : max_x = x
    if min_x > x : min_x = x
maze_map_x = max_x - min_x
maze_map_y = max_y - min_y
maze_map = [["#"]*(maze_map_x+1) for _ in range(maze_map_y+1)]
for i in range(len(way_point)) : 
    way_point[i][0] = (way_point[i][0]+abs(min_y))%(maze_map_y+1)
    way_point[i][1] = (way_point[i][1]+abs(min_x))%(maze_map_x+1)
    # print(y,x)

for y in range(maze_map_y+1):
    for x in range(maze_map_x+1):
        if [y,x] in way_point:
            maze_map[y][x] = "."
# print(maze_map)
for i in range(maze_map_y,-1,-1):
    print(''.join(maze_map[i]))



