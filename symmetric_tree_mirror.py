from symbol import and_expr
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: Optional[TreeNode]) -> bool:
    def dfs(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and
          dfs(left.right, right.left) and
          dfs(left.left, right.right))

    return dfs(root.left, root.right)



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    print(isSymmetric(root))