def bisectionMethod(function , aInterval , bInterval ):
    faInterval = f(aInterval)
    fbInterval = f(bInterval)

    if faInterval * fbInterval > 0:
        print("f(a) and f(b) Must Be Different Signs To Find The root ")
        return None

    for _ in range(100):  # 100 iteration
        c = (aInterval + bInterval) / 2
        fc = f(c)

        if fc == 0:
            return c
        if faInterval * fc > 0:
            aInterval = c
            faInterval = fc
        if fbInterval * fc > 0:
            bInterval = c
            fbInterval = fc

    return c


f = lambda x: x ** 3 -x -1

aInterval = 1
bInterval = 4
print(f"From : {aInterval}")
print(f"To : {bInterval}")
root= bisectionMethod(f, aInterval, bInterval)

print(f"Solution   :  {root}")
print("--------------------")
aInterval = 3
bInterval = 7

print(f"From : {aInterval}")
print(f"To : {bInterval}")

root= bisectionMethod(f, aInterval, bInterval)

print(f"Solution   :  {root}")