import sys

class Node:
    def __init__(self, n):
        self.n = n
        self.children = []
        self.height = None

def compute_height(n, parents):
    uzs = [uz(i) for i in range(n)]
    r = None

    for i, p in enumerate(parents):
        if p == -1:
            r = uzs[i]
        else:
            uzs[p].children.append(uzs[i])

    if r is None:
        return 0

    storage = [(r, 1)]
    max_height = 0
    while storage:
        uz, height = storage.pop()
        uz.height = height
        max_height = max(max_height, height)
        storage.extend([(child, height + 1) for child in uz.children])

    return max_height

def main():
    text = input()
    if 'F' in text and not 'a' in text:
        name = input()
        file = "./test/" + name
        with open(file) as f:
            num = f.readline()
            text = f.readline()
    if 'I' in text:
        num = input()
        text = input()
    print(compute_height(int(num), list(map(int, text.split()))))

if __name__ == '__main__':
    sys.setrecursionlimit(10**7)  
    main()
