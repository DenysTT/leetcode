"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

  
    def maxDepth(self, root):
        if not root:
            return False
        queue = [root]
        count = 0
        while queue:
            count += 1
            for i in queue:
                if i.right:
                    queue.append(i.right)
                if i.left:
                    queue.append(i.left)
            queue.pop(0)
        return count