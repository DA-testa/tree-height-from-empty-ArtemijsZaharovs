# python3
def depth(uz, vec):
    if vec[uz] == -1:
        return 1
    else:
        return 1 + depth(vec[uz], vec)

def heights(k, vec):
    height = 0
    for i in range(k):
        height = max(height, depth(i, vec))
    return height

k = int(input())
vec = list(map(int, input().split()))

print(heights(k, vec))




