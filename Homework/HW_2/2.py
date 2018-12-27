def solution1(arg):
    return [4*ch for ch in arg]
def solution2(arg):
    return [(i+1)*ch for i, ch in enumerate(arg)]
def solution3(arg):
    return [i for i in arg if i%3==0 or i%5==0]
def solution4(arg):
    return [j for i in arg for j in i]           
def solution5(arg):
    return [(m,k,l) for m in range(1,arg+1) for k in range(m,arg+1) for l in range(k,arg+1) if m*m+k*k==l*l]
def solution6(arg):
    return [[j+i for j in arg[1]] for i in arg[0]]
def solution7(arg):
    return [[row[i] for row in arg] for i in range(len(arg[0]))]
def solution8(arg):
    return [[int(j) for j in ch.split(' ')] for ch in arg]
def solution9(arg):
    return {chr(k-min(arg)): (k-ord('a'))**2 for k in range(ord('a')+min(arg),1+ord('a')+max(arg))}
def solution10(arg):
    return {name.capitalize() for name in arg if len(name)>3}
solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}