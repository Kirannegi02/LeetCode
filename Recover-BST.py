class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = TreeNode(-2 ** 31 -1)
        node1, node2 = None, None
        stack = []
        curr = root
        while curr != None or stack:
            while curr != None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if curr.val < prev.val:
                if node1:
                    node1.val, curr.val = curr.val, node1.val
                    return
                else:
                    node1 = prev
                    node2 = curr
            prev = curr
            curr = curr.right
        node1.val, node2.val = node2.val, node1.val