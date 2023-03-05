class TreeNode:
    def __init__(self, num):
        self.num = num
        self.children = []
        self.depth = None

def depths(n, vecs):
    uz = [TreeNode(i) for i in range(n)]
    r = None

    for i, p in enumerate(vecs):
        if p == -1:
            r = uz[i]
        else:
            uz[p].children.append(uz[i])

    if r is None:
        return 0

    cx = [(r, 0)]  # start from depth 0
    max_depth = 0
    while cx:
        node, depth = cx.pop()
        node.depth = depth
        max_depth = max(max_depth, depth)
        for child in node.children:
            cx.append((child, depth + 1))

    return max_depth + 1  # add 1 to get the depth of the tree

def parse_input(input_string):
    input_lines = input_string.strip().split("\n")
    n = int(input_lines[0])
    vecs = list(map(int, input_lines[1].split()))
    return n, vecs

def solve(input_string):
    n, vecs = parse_input(input_string)
    return str(depths(n, vecs))

# example usage:
input_string = '5\n4 -1 4 1 1\n'
print(solve(input_string))
