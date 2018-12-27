import pandas as pd
import numpy as np
def peak_finder(s):
    result = []
    for i in s.index:
        if i>0 and i<max(s.index):
            if s[i]>s[i-1] and s[i]>s[i+1]:
                result.append(i)
    result = np.array(result)            
    return result            
