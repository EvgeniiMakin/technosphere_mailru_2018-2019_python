y = int(input())
if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
    print(0)
else:
    print(1)