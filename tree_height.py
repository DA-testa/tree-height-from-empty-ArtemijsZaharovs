import sys

class Node:
def init(self, n):
self.n = n
self.vec = []
self.height = None

def heights(n, vecs):
uz = [Node(i) for i in range(n)]
r = None
for i, p in enumerate(vecs):
    if p == -1:
        r = uz[i]
    else:
        uz[p].children.append(uz[i])

if r is None:
    return 0

sx = [(r, 1)]
max_height = 0
while sx:
    node, height = sx.pop()
    node.height = height
    max_height = max(max_height, height)
    for child in node.children:
        sx.append((child, height + 1))

return max_height
def main():
text = input()
if 'F' in text and not 'a' in text:
name = input()
file = "./test/" + name
with open(file) as f:
cip = f.readline()
text = f.readline()
if 'I' in text:
cip = input()
text = input()
print(heights(int(cip), list(map(int, text.split()))))

sys.setrecursionlimit(10**7)
main()
