class TreeNode:
    def __init__(self, num):
        self.num = num
        self.children = []
        self.depth = None

def compute_depth(n, parents):
    nodes = [TreeNode(i) for i in range(n)]
    root = None

    for i, p in enumerate(parents):
        if p == -1:
            root = nodes[i]
        else:
            nodes[p].children.append(nodes[i])

    if root is None:
        return 0

    stack = [(root, 1)]
    max_depth = 0
    while stack:
        node, depth = stack.pop()
        node.depth = depth
        max_depth = max(max_depth, depth)
        for child in node.children:
            stack.append((child, depth + 1))

    return max_depth

def parse_input(input_string):
    input_lines = input_string.strip().split("\n")
    n = int(input_lines[0])
    parents = list(map(int, input_lines[1].split()))
    return n, parents

def solve(input_string):
    n, parents = parse_input(input_string)
    return str(compute_depth(n, parents))

input_string = '7\n-1 0 0 1 1 2 2\n'
print(solve(input_string))
