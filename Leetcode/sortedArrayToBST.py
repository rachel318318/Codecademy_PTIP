# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, lst, lower, upper):
        if lower == upper:
            return
        
        mid = (lower+upper) // 2
        node = TreeNode(lst[mid])
        node.left = self.helper(lst,lower,mid)
        node.right = self.helper(lst,mid+1,upper)
        return node
    
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return []
        return self.helper(nums,0,len(nums))
