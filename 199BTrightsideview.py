import Optional, List, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        if not root: return out

        queue = deque()
        queue.append(root)

        while len(queue) != 0:
            size = len(queue)

            for i in range(size):
                node = queue[0]
                queue.popleft()
                if node.left is not None: queue.append(node.left)
                if node.right is not None: queue.append(node.right)

                if i == size-1:
                    out.append(node.val)

        return out