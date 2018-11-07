def binomial(n):
    for i in range(0,n+1):
        C = C*(n+1-i)//i if i>0 else 1
        yield str(C)
if __name__ == '__main__':
    for num in map(int, input().split()):
        print(' '.join(binomial(num)))