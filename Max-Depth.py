class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative Solution (BFS)
        if not root:
            return 0
        queue = []
        depth = 0
        
        queue.append(root)
        queue.append(None)
        
        while len(queue) > 0:
            node = queue.pop(0)
            if node == None:
                depth += 1
                queue.append(None)
                if queue[0] == None:
                    break
                continue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return depth