# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp = TreeNode(val)
        
        if not root:
            return temp
    
        curr = root
       
        while curr is not None:
            if curr.left is not None and val < curr.val :
                curr = curr.left
            elif curr.right is not None and val > curr.val:
                curr = curr.right
            else:
                break

        if curr.val > val:
            curr.left = temp
        else:
            curr.right = temp
    
        return root

        