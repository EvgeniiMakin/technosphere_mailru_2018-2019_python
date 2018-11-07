def ackermann(m,n):
    setattr(ackermann, 'counter', 0)   
    def acker(m,n):
        ackermann.counter+=1
        if m==0:
            return n+1
        elif (m>0) & (n==0):
            return acker(m-1,1)
        else:
            return acker(m-1,acker(m,n-1))
    return acker(m,n)  