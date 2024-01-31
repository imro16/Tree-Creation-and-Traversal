from typing import List

class Node:
    def __init__(self, val: int, children: List['Node'] = None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    @staticmethod
    def createTree(input: List[int]) -> Node:
        if not input:
            return None
        
        root = Node(input[0])
        stack = [root]
        i = 2  # Start from the second element
        
        while i < len(input):
            if input[i] is None:
                stack.pop()
            else:
                node = Node(input[i])
                stack[-1].children.append(node)
                stack.append(node)
            i += 1
        
        return root
    
    @staticmethod
    def traverseTree(root: Node) -> List[int]:
        def postorder(node, result):
            if node:
                for child in node.children:
                    postorder(child, result)
                result.append(node.val)
        
        result = []
        postorder(root, result)
        return result

i1 = input('Enter array with comma(",") separated: ')
input1 = [int(x) if x.isdigit() else None for x in i1.split(",")]
tree1 = Solution.createTree(input1)
print("Output", Solution.traverseTree(tree1))


