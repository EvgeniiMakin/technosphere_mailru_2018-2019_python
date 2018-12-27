def solution1(arg):
    import re
    return list(map(lambda x: int((re.sub('[^0-9]','', x))[::-1]), arg))
def solution2(arg):
    return list(map(lambda x: x[0]*x[1], arg))
def solution3(arg):
    return list(filter(lambda x: x%6 in {0,2,5}, arg))
def solution4(arg):
    return list(filter(None, arg))         
def solution5(arg):
    import operator
    for a in arg:
        operator.setitem(a,'square',a['width']*a['length'])
    return arg
def solution6(arg):
    import operator
    arg = arg.copy()
    for a in arg:
        operator.setitem(a,'square',a['width']*a['length'])
    return arg
def solution7(arg):
    import operator
    res = []
    for a in arg:
        new_a = a.copy()
        operator.setitem(new_a,'square',a['width']*a['length'])
        res.append(new_a)
    return res
def solution8(arg):
    from functools import reduce
    return (reduce(lambda x, y: x+y,[s['height'] for s in arg]), len(arg))
def solution9(arg):
    return list(map(lambda x: x['name'],[x for x in arg if x['gpa'] > 4.5]))
def solution10(arg):
    return list(filter(lambda x: sum(map(int,x[0::2]))==sum(map(int,x[1::2])),arg))
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