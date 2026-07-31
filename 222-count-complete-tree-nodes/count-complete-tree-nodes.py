# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        # Function to compute the depth of the leftmost path
        def leftDepth(node):
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth

        # Function to compute the depth of the rightmost path
        def rightDepth(node):
            depth = 0
            while node:
                depth += 1
                node = node.right
            return depth

        left = leftDepth(root)
        right = rightDepth(root)

        # If left and right depths are equal, it's a perfect binary tree
        if left == right:
            return (1 << left) - 1  # 2^depth - 1 nodes

        # Otherwise, recursively count nodes in left and right subtrees
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
