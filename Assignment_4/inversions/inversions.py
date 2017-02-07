# Uses python3
import sys

def inversions_calc(input_list, length):

    """
    Recursive function that splits input list into single unit
    lists, and then merges them back together
    """

    if length < 2:
        #print('the end', input_list)
        return input_list, 0

    #print('called again', input_list)

    half = length//2                                        # My center choosing is the problem!!

    left, left_inversions = inversions_calc(input_list[0 : half], half)
    right, right_inversions = inversions_calc(input_list[half : length], length - half)

    sorted_merge, inversions = i_merge(left, right, half, length-half)

    total_inversions = left_inversions + right_inversions + inversions

    return sorted_merge, total_inversions

def i_merge(left, right, left_length, right_length):

    """
    Merges input lists, and counts inversions while doing so.
    Returns a sorted merged list and number of inversions counted
    from this particular merge procedure
    """

    #print('merging', left, right)

    merge = []

    inversion_count = 0

    for element in range(left_length + right_length):

        if left[0] <= right[0]:

            merge.append(left[0])
            del left[0]
            left_length = left_length - 1

        else:

            inversion_count = inversion_count + len(left)
            merge.append(right[0])
            del right[0]
            right_length = right_length - 1

        if left_length < 1:

            merge = merge + right
            return merge, inversion_count

        if right_length < 1:

            merge = merge + left
            return merge, inversion_count

    return merge, inversion_count

'''def get_number_of_inversions(a, b, left, right):

    b = len(a) * [0]
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions

    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here

    half_1 = a[left: ave]
    half_2 = a[ave: right]
    len_1 = len(half_1)
    len_2 = len(half_2)

    for i in range((len(a))):

        if len(half_1) == 0:

            b.append(half_2)
            break

        if len(half_2) == 0:
            b.append(half_1)
            break

        if half_1[0] > half_2[0]:

            b.append(half_1[0])
            del half_1[0]
            len_1 = len_1 -1
            number_of_inversions += len_2

        else:

            b.append(half_2[0])
            del half_2[0]
            len_2 = len_2 - 1


    return number_of_inversions'''

'''if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    sorted_list, num_inversions = inversions(a)
    print(sorted_list, num_inversions)'''

#example = [2, 3, 9, 2, 9, 5]
#sorted_list, num_inversions = inversions_calc(example, 6)
#print(sorted_list, num_inversions)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    sorted_list, num_inversions = inversions_calc(a, n)
    print(num_inversions)