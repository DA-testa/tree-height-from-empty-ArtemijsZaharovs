#221RDC035, Artemijs Zaharovs, 18.gr.
import sys
import sys
import numpy

def heights(num, vecs):
    height = [0 for i in range(num)]
    heig = 0
    for i in range(num):
        height = 0
        p = i
        while not (int(vecs[p]) == -1):
            if (height[p] != 0):
                height += height[p] 
                break
            height += 1
            p = int(vecs[p])
        height[i] = height
        height = max(heig, height[i])
    return heig + 1

def main():
    command = input()
    if "F" in command:
        file_name = input()
        pa = "test/" + file_name
        if not "a" in file_name:
            with open(pa, "r") as f:
                text = f.read()
            partitioned = text.partition("\n")
            num = int(partitioned[0])
            r = partitioned[2].split(" ")
            r = numpy.array(r)
            print(heights(num, r))
    elif "I" in command:
        num = int(input())
        vecs = input()
        r = vecs.split(" ")
        r = numpy.array(r)
        print(heights(num, r))

if __name__ == "__main__":
    main()
