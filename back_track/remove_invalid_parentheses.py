#! usr/bin/env python
# -*- coding: utf-8 -*-
"""
    remove_invalid_parentheses.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    删除无效的括号

    :author: jacklv :)
    :copyright: (c) 2018, Tungee
    :date created: 19-6-12 下午4:54
    :python version: 3.5

"""
from typing import List


class Solution:

    # 1.确认哪些括号需要移除(可进行剪枝优化,将开头和结尾的无效括号剔除)
    # 2.遍历字符串,移除括号
    # 3.检查剩余的字符串是否有效
    @staticmethod
    def remove_invalid_parentheses(s: str) -> List[str]:

        # start = time()

        length = len(s)
        left = 0
        while left < length and s[left] != '(':
            if s[left] == ')':
                s = s[:left] + s[left+1:]
                length -= 1
            else:
                left += 1
        right = len(s) - 1
        while right > left and s[right] != ')':
            if s[right] == '(':
                s = s[:right] + s[right+1:]
                length -= 1
                right -= 1
            else:
                right -= 1

        def get_invalid_parentheses(ss):
            remove_parentheses = []
            for word in ss:
                if word in ('(', ')'):
                    remove_parentheses.append(word)
                if ''.join(remove_parentheses[-2:]) == '()':
                    remove_parentheses = remove_parentheses[:-2]
            return remove_parentheses

        remove_parentheses = get_invalid_parentheses(s)

        # end = time()
        # print(end - start)
        # start = end

        def remove_parenthesis(remove_words, ss):

            result = []
            if not remove_words:
                return [ss]

            for i, _ in enumerate(ss):
                if len(ss[i:]) < len(remove_words):
                    break
                if i >= 1 and _ == ss[i-1]:
                    continue
                if _ == remove_words[0]:
                    temp = ss[:i] + ss[i+1:]
                    temp_remove_words = remove_words[1:]
                    if temp_remove_words:
                        result.extend(remove_parenthesis(temp_remove_words, temp))
                    else:
                        result.append(temp)

            return result

        result = remove_parenthesis(remove_parentheses, s)
        #
        # end = time()
        # print(end - start)
        # start = end

        valid_result = []
        result = list(set(result))
        for _ in result:
            if not get_invalid_parentheses(_):
                valid_result.append(_)
        #
        # end = time()
        # print(end - start)
        # start = end
        valid_result = list(set(valid_result))
        print(valid_result)

        return valid_result


if __name__ == '__main__':
    Solution.remove_invalid_parentheses("((()()()((()()(()((()))))))(((((")
