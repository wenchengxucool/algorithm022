class Solution(object):
    def levelOrder(self, root):
        result = [] #是一个全局的数组
        # 定义了一个递归函数，函数参数是根节点与级数。从0开始
        def traverse_node(node, level):
            if len(result) == level:
                result.append([]) # 一级加一个空list[]进去。
            result[level].append(node.val)
            for child in node.children:
                traverse_node(child, level + 1)

        if root:
            traverse_node(root, 0) #推第一块多米诺骨牌
        return result