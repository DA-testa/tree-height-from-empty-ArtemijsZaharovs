import sys
import sys
import numpy

def heights(n, vecs):
    possible_heights = [0 for i in range(n)]
    max_height = 0
    for i in range(n):
        height = 0
        p = i
        while not (int(vecs[p]) == -1):
            if (possible_heights[p] != 0):
                height += possible_heights[p] 
                break
            height += 1
            p = int(vecs[p])
        possible_heights[i] = height
        max_height = max(max_height, possible_heights[i])
    return max_height + 1

def main():
    command = input()
    if "F" in command:
        file_name = input()
        path = "test/" + file_name
        if not "a" in file_name:
            with open(path, "r") as f:
                text = f.read()
            partitioned = text.partition("\n")
            n = int(partitioned[0])
            r = partitioned[2].split(" ")
            r = numpy.array(r)
            print(heights(n, r))
    elif "I" in command:
        n = int(input())
        vecs = input()
        r = vecs.split(" ")
        r = numpy.array(r)
        print(heights(n, r))

if __name__ == "__main__":
    main()
