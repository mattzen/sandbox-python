from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def max_depth_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return 1 + max(
            self.max_depth_recursive(root.left),
            self.max_depth_recursive(root.right),
        )

    def max_depth_bfs(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = 0
        queue = deque([root])

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level

    def max_depth_dfs(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = 0
        stack = deque([(root, 1)])

        while stack:
            node, depth = stack.pop()

            if node:
                level = max(level, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return level
    
    def averageOfLevelsBFS(self, root : TreeNode):
        if(not root):
            return []
        queue = deque([root])
        result = []
        current_val = 0
        current_ctr = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                current_val += node.val
                current_ctr = i
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_val/(current_ctr + 1))
            current_val = 0
        return result
    
    def printLevelsBFS(self, root : TreeNode):
        if(not root):
            return []
        queue = deque([root])
        result = []
        current_level = []
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
            current_level = []
        return result
        
    def printInorder(self, root : TreeNode):
        if(not root):
            return
        self.printInorder(root.left)
        print(root.val)
        self.printInorder(root.right)
        
    def printPostorder(self, root : TreeNode):
        if(not root):
            return
        self.printPostorder(root.left)
        self.printPostorder(root.right)
        print(root.val)
        
    def printPreorder(self, root : TreeNode):
        if(not root):
            return
        print(root.val)
        self.printPreorder(root.left)
        self.printPreorder(root.right)


# Test cases
sol = Solution()

tree = TreeNode(10)
tree.left = TreeNode(8)
tree.right = TreeNode(15)
tree.right.right = TreeNode(20)
tree.left.right = TreeNode(9)
tree.left.left = TreeNode(6)
tree.left.left.left = TreeNode(5)
tree.left.left.right = TreeNode(7)

sol.printPreorder(tree)

print(sol.averageOfLevels(tree))
print(sol.printLevels(tree))


assert sol.max_depth_recursive(tree) == 3
assert sol.max_depth_bfs(tree) == 3
assert sol.max_depth_dfs(tree) == 3

tree = TreeNode(1)
tree.right = TreeNode(2)

assert sol.max_depth_recursive(tree) == 2
assert sol.max_depth_bfs(tree) == 2
assert sol.max_depth_dfs(tree) == 2