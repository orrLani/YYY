
import numpy as np
import matplotlib.pyplot as plt


import sys
sys.setrecursionlimit(50000)

# def fill_array(array,x,y):
#     if array[x][y] == 1 or  array[x][y] == 2:
#         return
#
#     if array[x][y] == 0:
#         array[x][y] = 2
#
#     fill_array(array, x , y-1)
#     fill_array(array,x+1,y)
#     fill_array(array, x , y+1)
#     fill_array(array, x-1 , y)

if __name__ == '__main__':
    a = 'data: "[2.4, 0.3][-1.0, -2.3]"'
    dirty_location = []
    string_dirty_list = eval(a.split(':')[1]).split(']')

    for index in range(0, len(string_dirty_list)-1):
        val = string_dirty_list[index].split('[')[1].split(',')
        loc = np.array([float(val[0]),float(val[1])])
        print(loc)


    # array = np.load('array.npy')
    # temp_array = array.copy()
    # fill_array(temp_array,199,199)
    # np.where(temp_array == 2)
    # plt.imshow(temp_array)
    # plt.show()
    # pass




