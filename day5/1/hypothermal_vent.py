from dataclasses import dataclass
from typing import List, Tuple

with open('input.txt') as f:
    data = f.readlines()


def minmax(a: int, b: int) -> Tuple[int, int]:
    if a <= b:
        return a, b
    return b, a


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Line:
    points: List[Point]


lines = []
min_x, min_y = 0, 0
max_x, max_y = 0, 0
for entry in data:
    x1y1, x2y2 = entry.strip().split(' -> ')
    x1, y1 = map(lambda n: int(n), x1y1.split(','))
    x2, y2 = map(lambda n: int(n), x2y2.split(','))
    if x1 != x2 and y1 != y2:
        continue
    _min_x, _max_x = minmax(x1, x2)
    _min_y, _max_y = minmax(y1, y2)
    r = Line([])
    for i in range(_min_x, _max_x + 1):
        for j in range(_min_y, _max_y + 1):
            p = Point(i, j)
            r.points.append(p)
    lines.append(r)
    min_x = min(_min_x, min_x)
    max_x = max(_max_x, max_x)
    min_y = min(_min_y, min_y)
    max_y = max(_max_y, max_y)

max_x += 1
max_y += 1

def calc_grid(lines: List[Line]):
    grid = []
    for i in range(max_x):
        grid.append([])
        for _ in range(max_y):
            grid[i].append(0)    
    for l in lines:
        for p in l.points:
            try:
                grid[p.y][p.x] += 1
            except IndexError:
                if p.y >= len(grid):
                    for i in range(p.y - len(grid) + 1):
                        grid.append([])
                        for _ in range(max_y):
                            grid[-1].append(0)
                elif p.x >= len(grid[0]):
                    for row in grid:
                        for _ in range(p.x - len(grid[0]) + 1):
                            row.append(0)
                grid[p.x][p.y] += 1

    return grid


grid = calc_grid(lines)
intersections = len(list(filter(lambda x: x >= 2, (i for l in grid for i in l))))
print(intersections)
