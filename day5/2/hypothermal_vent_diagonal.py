from dataclasses import dataclass
from typing import List, Tuple
from functools import cache


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Line:
    points: List[Point]


@cache
def minmax(a: int, b: int) -> Tuple[int, int]:
    if a <= b:
        return a, b
    return b, a


def calc_grid(lines: List[Line]):
    grid = []
    for i in range(max_x):
        grid.append([])
        for _ in range(max_y):
            grid[i].append(0)    
    for l in lines:
        for p in l.points:
            grid[p.x][p.y] += 1

    return grid


with open('input.txt') as f:
    data = f.readlines()

lines = []
min_x = 0
max_x = 0
min_y = 0
max_y = 0
stoi = lambda n: int(n)
for entry in data:
    x1y1, x2y2 = entry.strip().split(' -> ')
    x1, y1 = map(stoi, x1y1.split(','))
    x2, y2 = map(stoi, x2y2.split(','))

    _min_x, _max_x = minmax(x1, x2)
    _min_y, _max_y = minmax(y1, y2)
    min_x = min(_min_x, min_x)
    max_x = max(_max_x, max_x)
    min_y = min(_min_y, min_y)
    max_y = max(_max_y, max_y)

    r = Line([])
    if x1 != x2 and y1 != y2:
        if abs(x1 - x2) == abs(y1 - y2): # Diagonally aligned
            delta = abs(x1 - x2)
            d_x = -1 if x1 - x2 < 0 else 1
            d_y = -1 if y1 - y2 < 0 else 1
            start_x = _min_x if d_x > 0 else _max_x
            start_y = _min_y if d_y > 0 else _max_y
            for d in range(delta + 1):
                p = Point(start_x + d * d_x, start_y + d * d_y)
                r.points.append(p)
        else:
            continue
    else:
        for i in range(_min_x, _max_x + 1):
            for j in range(_min_y, _max_y + 1):
                p = Point(i, j)
                r.points.append(p)
    lines.append(r)

max_x += 1
max_y += 1

grid = calc_grid(lines)
intersections = 0
for l in grid:
    for i in l:
        if i >= 2:
            intersections += 1
print(intersections)
