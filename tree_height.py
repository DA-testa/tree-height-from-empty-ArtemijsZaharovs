import sys
import sys
import numpy

def max_chain_length(n, arr):
    chains = [0] * n
    for i in range(n):
        if arr[i] == -1:
            chains[i] = 1
        elif chains[arr[i]] == 0:
            chains[i] = max_chain_length(n, arr[arr[i]:]) + 1
        else:
            chains[i] = chains[arr[i]] + 1
    return max(chains)

def main():
    command = input().strip()
    if command == "I":
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(max_chain_length(n, arr))
    elif command == "F":
        file_name = input().strip()
        if "a" not in file_name:
            with open("test/" + file_name) as f:
                n = int(f.readline().strip())
                arr = [int(x) for x in f.readline().split()]
                print(max_chain_length(n, arr))

if __name__ == "__main__":
    main()
