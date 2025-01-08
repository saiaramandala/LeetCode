# Definition for a binary tree node
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def post_order_traversal(root: Optional[TreeNode]) -> List[int]:
    stack = [root] # Stack to hold nodes
    visit = [False] # Stack to track if we've visited a node twice

    res = [] # To store the result of the post-order traversal

    while stack:
       cur, v = stack.pop(), visit.pop()
       if cur:
           if v:
               # If we are visiting the node after its children, add it to result i.e it has been visited 2nd time
               res.append(cur.val)
           else:
               # Push the current node back onto the stack as we want to visit it later
               stack.append(cur)
               visit.append(True) # Mark this node to be visited after its children

               # Push right child, left child in the stack (order matters as you want left child first and then right child and this is a stack)
               stack.append(cur.right)
               visit.append(False)
               stack.append(cur.left)
               visit.append(False)

    return res # Return the post-order traversal result



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)


    # Perform post-order traversal
    result = post_order_traversal(root)
    print(result)



