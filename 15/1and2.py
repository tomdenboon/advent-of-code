import heapq
import time


def dijkstra(maze):
    heap = []
    visited = {}
    heapq.heappush(heap, (0, (0, 0)))
    while heap:
        dist, curr = heapq.heappop(heap)
        next = []
        next.append((curr[0] + 1, curr[1]))
        next.append((curr[0] - 1, curr[1]))
        next.append((curr[0], curr[1] + 1))
        next.append((curr[0], curr[1] - 1))
        for (i, j) in next:
            if i < len(maze) and i >= 0 \
                    and j < len(maze[i]) and j >= 0 \
                    and not (i, j) in visited:
                visited[(i, j)] = True
                alt = dist + maze[i][j]
                if len(maze) - 1 == i and len(maze[0]) - 1 == j:
                    return alt
                heapq.heappush(heap, (alt, (i, j)))


t1 = time.perf_counter()
maze = []
file = open('input')
for line in file:
    row = [int(x) for x in line.strip()]
    maze.append(row)

mazes = []
mazes.append(maze)
for x in range(8):
    new_maze = []
    for i in range(len(maze)):
        new_maze_row = []
        for j in range(len(maze[i])):
            new_maze_row.append((mazes[x][i][j] % 9) + 1)
        new_maze.append(new_maze_row)
    mazes.append(new_maze)
big_maze = []
for i in range(5):
    for x in range(len(mazes[0])):
        big_row = []
        for j in range(5):
            big_row = big_row + mazes[i+j][x]
        big_maze.append(big_row)
print(dijkstra(big_maze))
print(time.perf_counter() - t1)
