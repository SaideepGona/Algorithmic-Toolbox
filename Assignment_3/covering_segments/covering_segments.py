# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):

    points = segments
    ends = []
    #write your code here

    for s in segments:

        ends.append(s.end)

    ends, points = (list(t) for t in zip(*sorted(zip(ends, points))))

    end = points[0][1]
    answer = [end]

    for point in points:

        if point[0] > end:

            end = point[1]
            answer.append(end)

    return answer

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end= ' ')



