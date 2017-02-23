# Uses python3
import numpy as np

def edit_distance(string_hori, string_vert):
    #write your code here

    full_array = np.zeros((len(string_vert) + 1, len(string_hori) + 1))
    full_array[0,:] = np.arange(len(string_hori) + 1)
    full_array[:,0] = np.arange(len(string_vert) + 1)

    for hori_char in range(1, len(string_hori) + 1):

        for vert_char in range(1, len(string_vert) + 1):

            if string_hori[hori_char-1] == string_vert[vert_char-1]:

                min_val = full_array[vert_char - 1, hori_char - 1]

            else:

                min_array = [full_array[vert_char - 1, hori_char] + 1, full_array[vert_char, hori_char - 1] + 1, full_array[vert_char - 1, hori_char - 1] + 1]
                min_val = min(min_array)

            full_array[vert_char, hori_char] = min_val

    return int(full_array[len(string_vert), len(string_hori)])

'''
str1 = 'short'
str2 = 'ports'

x = edit_distance(str1, str2)
print(x)

'''
if __name__ == "__main__":
    print(edit_distance(input(), input()))
