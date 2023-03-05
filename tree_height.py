# python3
def height(k, vec ):
    kok = [[] for _ in range(k)]
    for ber, vect in enumerate(vec):
        if vect == -1:
            r = ber
        else:
            kok[vect].append(ber)

   
    def height(uz, x):
     
        if x[uz]:
            return x[uz]
        
        if not kok[uz]:
            x[uz] = 1
            return 1
 x[node] = max(height(ber, x) for ber in kok[uz]) + 1
        return x[node]

    x = [0] * k
    return height(r, x)

k = 5
vec = [4, -1, 4, 1, 1]
print(height(k, vec))  
