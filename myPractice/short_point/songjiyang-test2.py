#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
思路：
1.先找两个最近的点作为已连接列表
2.遍历剩下的点，找离已连接列表里面的点最近的一个点，两层迭代，加入已连接列表
3.重复2遍历其他的点
"""
import matplotlib.pyplot as plt
import numpy as np
from random import randint


def get_distince(p1, p2):
    return (p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2


def short_point(point_list):
    connected_point_list = list()
    min_distince = float('inf')
    min_index = float('inf')
    # 找第一个点和离它最近的点
    for i, i_point in enumerate(point_list):
        if 0 == i:
            continue
        distince = get_distince(point_list[0], i_point)
        if distince < min_distince:
            min_distince = distince
            min_index = i
    connected_point_list.append((0, min_index))

    connected_index_list = [0, min_index]
    # 迭代剩下的点
    while len(connected_index_list) < len(point_list):
        # 求所有点中与已连接列表最近的点
        closest_distince = float('inf')
        closest_connected_point_index = None
        closest_unconnect_point_index = None
        for i, point in enumerate(point_list):
            if i in connected_index_list:
                continue
            for connected_point in connected_point_list:
                left_point = point_list[connected_point[0]]
                right_point = point_list[connected_point[1]]
                unconnect_point = point
                left_distince = get_distince(left_point, unconnect_point)
                right_distince = get_distince(right_point, unconnect_point)
                # print '未连接点到连接点', i, point, left_point, right_point
                # print '左距离%s,右距离%s' % (left_distince, right_distince)
                if left_distince < closest_distince:
                    closest_distince = left_distince
                    closest_connected_point_index = connected_point[0]
                    closest_unconnect_point_index = i
                if right_distince < closest_distince:
                    closest_distince = right_distince
                    closest_connected_point_index = connected_point[1]
                    closest_unconnect_point_index = i
        # print '已连接列表为：', connected_point_list
        # print '距离已连接列表最近的点为', closest_unconnect_point_index, point_list[
        #     closest_unconnect_point_index]
        connected_point_list.append(
            (closest_connected_point_index, closest_unconnect_point_index))
        connected_index_list.append(closest_unconnect_point_index)
    return connected_point_list


def show_result(input, output):
    x = [o[0] for o in input]
    y = [o[1] for o in input]
    n = np.arange(len(input))
    fig, ax = plt.subplots()
    ax.scatter(x, y, c='r')
    for i, txt in enumerate(n):
        ax.annotate(txt, (x[i], y[i]))
    for c in output:
        ax.plot([x[c[0]], x[c[1]]], [y[c[0]], y[c[1]]])
    plt.show()


if __name__ == '__main__':
    input = [[63, 79], [97, 41], [60, 58], [72, 98], [84, 60], [4, 61],
             [81, 85], [17, 76]]
    # input = [[randint(1, 100), randint(1, 100)] for i in xrange(10)]
    print '输入', input
    output = short_point(input)
    print '输出', output

    show_result(input, output)
