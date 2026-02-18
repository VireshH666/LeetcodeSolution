# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        self.inorder(root,res,k)
        return res[-1]

    def inorder(self,curr,res,k):
        if curr is None:
            return
        self.inorder(curr.left,res,k)
        if k == len(res):
            return
        else:
            res.append(curr.val)            
        self.inorder(curr.right,res,k)
