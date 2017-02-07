# Uses python3
import sys

def divide_check(dividend, divisor):

    if dividend % divisor == 0:
        return True
    else:
        return False

def div_int(dividend, divisor):

    return int(dividend/divisor)

def smallest_check(list):

    change_val = 3
    mini = min(list)
    min_index = list.index(min)

    if min_index == 1:
        change_val = 2
    if min_index == 2:
        change_val = 1

    return (mini, change_val)

def path_add(change_val, current_val):

    path_val = 0

    if change_val == 3 or 2:
        path_val = int(current_val/change_val)
    else:
        path_val = int(current_val-1)

    return path_val

# Main

def prim_calc(n):

    def create(num):

        Buildup_List = [0,0]
        Path_List = [0,0]
        High = num + 1

        for current in range(2, num):

            Previous_Buildup = []

            if divide_check(current, 3):
                Previous_Buildup.append(Buildup_List[div_int(current, 3)])
            else:
                Previous_Buildup.append(High)
            if divide_check(current, 2):
                Previous_Buildup.append(Buildup_List[div_int(current, 2)])
            else:
                Previous_Buildup.append(High)
            Previous_Buildup.append(Buildup_List[current - 1])

            pass_on = smallest_check(Previous_Buildup)
            Buildup_List.append(pass_on[0] + 1)
            Path_List.append(path_add(pass_on[1],current))

        return Path_List

    def back_prop(Path_List):

        Current_El = Path_List[-1]
        Path = []

        while Current_El != 1:

            Path.append(Current_El)
            Next_El = Current_El
            Current_El = Path_List[Next_El]

        return Path

    Path_List_Pre = create(n)
    Final_Path = back_prop(Path_List_Pre)

    return Final_Path


#input = sys.stdin.read()
#n = int(input)
n = 5
sequence = list(prim_calc(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
