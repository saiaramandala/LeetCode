# Definition for a binary tree node
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order_traversal(root: Optional[TreeNode]) -> List[int]:
    cur, stack = root, []
    res = []

    while cur or stack:
        if cur:
            res.append(cur.val)
            stack.append(cur.right)
            cur = cur.left
        else:
            cur = stack.pop()
    return res

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)


    # Perform post-order traversal
    result = pre_order_traversal(root)
    print(result)

    # time complexity: O(n)
    # space complexity: worst case: O(n) , best case: O(log n)