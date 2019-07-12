#! usr/bin/env python
# -*- coding: utf-8 -*-
"""
    trie.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    208. 实现 Trie (前缀树)

    :author: jacklv :)
    :copyright: (c) 2018, Tungee
    :date created: 19-7-9 下午8:56
    :python version: 3.5

"""


class Node:

    def __init__(self, val):
        """
        Initialize a node.
        """
        self._val = val
        self._is_end = False
        self._val_to_child_node_dict = dict()

    def add_child_node(self, val):
        """
        add a child node
        :param val:
        :return:
        """
        # if val already exists in child nodes, return that
        if val not in self._val_to_child_node_dict:
            self._val_to_child_node_dict[val] = Node(val)

        return self._val_to_child_node_dict[val]

    def get_child_node(self, val):
        """
        Get a child node by a certain value
        :param val:
        :return:
        """
        return self._val_to_child_node_dict.get(val, None)

    def mark_as_end(self):
        """
        mark as end node
        :return:
        """
        self._is_end = True

    @property
    def val(self):
        """
        Get val of node.
        :return:
        """
        return self._val

    @property
    def end(self):
        """
        If end
        :return:
        """
        return self._is_end


class Trie:

    # 解法1,采用节点,效率不高------

    # def __init__(self):
    #     """
    #     Initialize your data structure here.
    #     """
    #     self._root_node = Node(None)
    #
    # def insert(self, word: str) -> None:
    #     """
    #     Inserts a word into the trie.
    #     """
    #     if word:
    #         last_node = self._root_node
    #         for char in word:
    #             last_node = last_node.add_child_node(char)
    #
    #         # last node should be a end node
    #         last_node.mark_as_end()
    #
    # def search(self, word: str) -> bool:
    #     """
    #     Returns if the word is in the trie.
    #     """
    #     last_node = self._root_node
    #     for char in word:
    #         last_node = last_node.get_child_node(char)
    #         if not last_node:
    #             return False
    #
    #     if last_node.end:
    #         return True
    #     else:
    #         return False
    #
    # def startsWith(self, prefix: str) -> bool:
    #     """
    #     Returns if there is any word in the trie that starts with the given prefix.
    #     """
    #     last_node = self._root_node
    #     for char in prefix:
    #         last_node = last_node.get_child_node(char)
    #         if not last_node:
    #             return False
    #
    #     return True

    # end------

    # 解法2,通过字典方式实现节点
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if word:
            last_node = self._trie
            for i, char in enumerate(word):
                if char not in last_node:
                    last_node[char] = {}
                last_node = last_node[char]

            last_node['is_end'] = True

        print(self._trie)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        last_node = self._trie
        for char in word:
            last_node = last_node.get(char, {})
            # print(last_node)
            if not last_node:
                return False

        if last_node.get('is_end'):
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        last_node = self._trie
        for char in prefix:
            last_node = last_node.get(char, {})
            if not last_node:
                return False

        return True

if __name__ == '__main__':
    obj = Trie()
    obj.insert('app')
    obj.insert('apple')
    obj.insert('bear')
    obj.insert('add')
    obj.insert('jam')
    obj.insert('rental')
    # obj.search('apps')
    print(obj.search('app'))