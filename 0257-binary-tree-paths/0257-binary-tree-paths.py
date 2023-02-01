# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]: # O(N) time | O(N) space [worst case: linear tree] O(logN) space [best case: balanced tree]
#         paths = []
        
#         def dfs(root, path):
#             if root:
#                 path += str(root.val)
                
#                 if not root.left and not root.right:
#                     paths.append(path)
#                 else:
#                     path += '->'
#                     dfs(root.left,path)
#                     dfs(root.right,path)
                
#         dfs(root, '')
        
#         return paths
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: 
            return []
        
        stack = [(root, str(root.val))]
        paths = []
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
                
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
                
        
        return paths
    
    