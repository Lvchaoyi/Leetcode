#! usr/bin/env python
# -*- coding: utf-8 -*-
"""
    unique_path_III.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    980. 不同路径 III

    :author: jacklv :)
    :copyright: (c) 2018, Tungee
    :date created: 19-6-17 上午11:19
    :python version: 3.5

"""
from typing import List


class Solution:

    # 1.确定起点，终点，障碍
    # 2.从起点开始，不停遍历可达的下一个点（DFS），直到到达终点或者被阻塞，
    # 并返回路径(形如[(0,0), (1,0)]对应解空间)
    # 3.可达的路径数即为预期值
    @staticmethod
    def uniquePathsIII(grid: List[List[int]]) -> int:

        row_length = len(grid)
        col_length = len(grid[0])
        start, end = None, None
        blocks = set()
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                point = (i, j)
                if cell == 1:
                    start = point
                elif cell == 2:
                    end = point
                elif cell == -1:
                    blocks.add(point)

        def get_next_points(p):
            """
            获得下个可达点
            :param p: point 当前点
            :return:
            """
            x, y = p
            # 约束函数
            points = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
            points = [_ for _ in points if 0 <= _[0] < row_length and 0 <= _[1] < col_length]
            return points

        def traceback(s, e, b):
            """
            回溯，寻找接下来可达的若干个点
            :param s: start
            :param e: end
            :param b: begin
            :return:
            """

            available_paths = []
            if s in b:
                return available_paths

            next_points = get_next_points(s)
            if len(b) == row_length * col_length - 2 and e in next_points:
                available_paths = [[s, e]]
            else:
                c = b.copy()
                c.add(s)
                for next_point in next_points:
                    # 界限函数
                    if next_point in b or next_point == e:
                        continue
                    available_child_paths = traceback(next_point, e, c)
                    for available_child_path in available_child_paths:
                        available_child_path.insert(0, s)
                        available_paths.append(available_child_path)

            return available_paths

        # 解空间
        paths = traceback(start, end, blocks)
        path_count = len(paths)

        return path_count


if __name__ == '__main__':
    Solution.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]])
    # Solution.uniquePathsIII([[1,-1],[2,-1]])
