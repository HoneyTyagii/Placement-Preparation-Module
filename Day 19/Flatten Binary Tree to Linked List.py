# 114. Flatten Binary Tree to Linked List
# Medium

# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.

# Example 1:

# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [0]
# Output: [0]

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        def rightmost(root):
            if (root.right):
                return rightmost(root.right)
            return root
        
        if root:
            nextright = None
            rightMOST = None
        
        while root:
            if root.left:
                rightMOST = rightmost(root.left)
                nextright = root.right
                root.right = root.left
                root.left = None
                rightMOST.right = nextright
            root=root.right

# time complexity o(n)
# space complexity o(1)