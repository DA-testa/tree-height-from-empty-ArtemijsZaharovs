import os

def inputs():
    while True:
        method = input("(F for file, I for keyboard): ")
        if method.upper() == "F":
            filename = input("Enter filename: ")
            if "a" in filename:
                print("Invalid filename.")
            elif os.path.exists(f"inputs/{filename}"):
                with open(f"inputs/{filename}", "r") as f:
                    return f.read().strip().split("\n")[1:]
            else:
                print("File not found. ")
        elif method.upper() == "I":
            n = int(input("Enter  "))
            vec = list(map(int, input("Enter  ").split()))
            return n, vec
        else:
            print("Invalid input method. ")

def heights(n, vec):
    uz = [[] for i in range(n)]
    for i in range(n):
        if vec[i] == -1:
            r = i
        else:
            uz[vec[i]].append(i)
    aug = 0
    q = [(r, 1)]
    while q:
        node, level = q.pop(0)
        aug = max(aug, level)
        for ber in uz[node]:
            q.append((ber, level + 1))
    return aug

if __name__ == "__main__":
    n, vec = inputs()
    aug = heights(n, vec)
    print(aug)
