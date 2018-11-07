import pandas as pd
def df_diag_ones(data):
    N,M = data.shape
    for i in range(N):
        for j in range(M):
            if i == j or (i+j)==N-1:
                data[i][j]=1
    return data        
