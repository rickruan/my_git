#coding: utf8

def getPrime(max):
    aList = [True for x in range(0, max)]
    prime = []
    for x in range(2, max):
        if aList[x]:
            prime.append(x)
            for y in range(2, (max//x)+1):
                if x * y < max:
                    aList[x * y] = False
    return prime

print(getPrime(512))