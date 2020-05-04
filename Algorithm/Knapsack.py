import numpy as np


def _pick_method(n, m, space_list, select_mat):
    curr_m = m
    method = []
    for i in range(n, 0, -1):
        method.append(select_mat[i, curr_m])
        curr_m -= space_list[i-1]*select_mat[i, curr_m]
    return list(reversed(method))


def knapsack_01(bag_size, space_list, weight_list):
    n, m = len(space_list), bag_size
    value_mat = np.zeros((n+1, m+1))
    select_mat = np.zeros((n+1, m+1), dtype="int")
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if space_list[i-1] > j:
                value_mat[i, j] = value_mat[i-1, j]
            else:
                pick_value = weight_list[i-1] + value_mat[i-1, j-space_list[i-1]]
                unpick_value = value_mat[i-1, j]
                value_mat[i, j] = max(pick_value, unpick_value)
                select_mat[i, j] = 1 if pick_value > unpick_value else 0
    method = _pick_method(n, m, space_list, select_mat)
    return value_mat[n, m], method

if __name__ == "__main__":
    bag_size = 4
    space_list = [1, 4, 3]
    weight_list = [1500, 3000, 2000]
    max_value, select_method = knapsack_01(4, space_list, weight_list)
    print(max_value, select_method)