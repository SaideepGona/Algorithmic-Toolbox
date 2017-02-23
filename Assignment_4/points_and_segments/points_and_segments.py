# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    '''
    Fast - O(nlogn) - points and segments algorithm
    '''
    values = starts + ends + points
    identities = list(len(starts)*'s') + list(len(ends)*'e') + list(len(points)*'p')
    tup_sorted_values, sorted_identities = zip(*sorted(zip(values, identities)))

    current_score = 0
    current_ends = 0
    unique_vals = []
    scores = []
    final = []
    sorted_values = list(tup_sorted_values)
    sorted_values.append(float("inf"))

    for index in range(len(sorted_identities)):

        if sorted_identities[index] == 's':
            current_score = current_score + 1

        elif sorted_identities[index] == 'e':
            current_score = current_score - 1
            current_ends = current_ends + 1

        if sorted_values[index+1] != sorted_values[index]:
            unique_vals.append(sorted_values[index])
            scores.append(current_score+current_ends)
            current_ends = 0

    scores.append(current_score)

    points_ind = range(len(points))
    sorted_points, sorted_points_ind = zip(*sorted(zip(points, points_ind)))
    sorted_points = list(sorted_points)

    for point_index in range(len(sorted_points)):

        while sorted_points[point_index] != unique_vals[0]:
           del unique_vals[0]
           del scores[0]

        final.append(scores[0])
    
    return_to_points_ind, final_sorted = zip(*sorted(zip(sorted_points_ind, final)))
    final_sorted = list(final_sorted)

    return final_sorted
'''    
def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt
'''

exstarts = [1,-4]
exends = [5, 2]
expoints = [-4, -4, 2, 10, -4]

out = fast_count_segments(exstarts, exends, expoints)
print(expoints)
print(out)
'''
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
'''