import numpy as np
def zeros_insert(k,n):
    new = list()
    for i in k:
        new.append(float(i))
        for i in range(n):
            new.append(0.)
    for i in range(n):
        new.pop()
    new = np.array(new)    
    
    return new