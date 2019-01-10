#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
思路：
一、先找到第一个点和离它最近的一个点，然后形成一条直线，这边直接可能有三种情况
1.与x轴垂直
2.与y轴垂直
3.有斜率的直线
二、然后连接一个新的点，对应上面的情况做出如下措施，然后加入已连接的点的列表
1.比较新的点的纵坐标与上面直线的中点的纵坐标，小的话靠近下面的点，大的话靠近上面的点
2.比较新的点的横坐标与上面直线的中点的横坐标，小的话靠近左边的点，大的话靠近右边的点
3.比较新的点坐标纵坐标代入上面垂直平分线的纵坐标，当k>0时，新的纵坐标大靠近左上的点，小则靠近右下的点，k<0时，新的的纵坐标大靠近右上的点，小则靠近左下的点
三、在连接两个点之后，连接第三个点，第三个点先与第一个点作二操作取靠近的点，
然后发现已连接的点的列表中这个点还和其他点相连，继续做二操作，直到这个列表中没有它获取到的最靠近的点
"""


def line_func(k, d):

    def func(point):
        if k > 0:
            return point[1] >= k * point[0] + d
        else:
            return point[1] <= k * point[0] + d
    return func


def get_func(p1, p2):
    # 求垂直平分线
    # 求斜率
    if p1[0] < p2[0]:
        p1, p2 = p2, p1
    # 与纵轴垂直的线
    if float(p1[1] - p2[1]) == 0:
        mid = float(p1[0] + p2[0]) / 2.0
        return lambda point: True if point[0] < mid else False
    # 与横轴垂直的线
    elif float(p1[0] - p2[0]) == 0:
        mid = float(p1[1] + p2[1]) / 2.0
        return lambda point: True if point[1] < mid else False
    else:
        k = - 1 / (float(p1[1] - p2[1]) / float(p1[0] - p2[0]))
        # 求中点的位置
        mid = (float(p1[0] + p2[0]) / 2.0, float(p1[1] + p2[1]) / 2.0)
        # d = y - kx
        d = mid[1] - k * mid[0]
        return line_func(k, d)


def short_point(test_data):
    point_list = test_data
    if not point_list:
        return []
    lines_list = list()
    first = point_list[0]
    connected_point = dict()
    min_value = float('inf')
    min_index = 0
    min_point = None
    # 先求第一个点和离他最近的点
    for i in range(1, len(point_list) - 1):
        point = point_list[i]
        value = (point[1] - first[1]) ** 2 + (point[0] - first[0]) ** 2
        if value < min_value:
            min_value = value
            min_index = i
            min_point = point

    lines_list.append([0, min_index])
    connected_point[(0, min_index)] = get_func(first, min_point)
    for i, point in enumerate(point_list):
        if i == 0 or i == min_index:
            continue
        connecting_point_index = None
        for connected, func in connected_point.iteritems():
            if not connecting_point_index or connecting_point_index in connected:
                if func(point):
                    connecting_point_index = connected[0]
                else:
                    connecting_point_index = connected[1]
        connected_point[(connecting_point_index, i)] = \
            get_func(point_list[i], point_list[connecting_point_index])
    return connected_point.keys()

if __name__ == '__main__':

    test_data = [
        [[1, 1], [2, 2], [3, 3]],
        [[0, 0], [4, 0], [6, -2], [7, 4]],
        [[0, 0], [0, 5], [5, 0], [6, -1]],
        []
    ]
    for data in test_data:

        print '输入', data
        print '输出', short_point(data)
