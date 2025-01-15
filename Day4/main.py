import sys
import hashlib

f = open("Input.txt", "r")
content = f.read()


def getHash(c, counter):
    m = (hashlib.md5((c + str(counter)).encode()))
    return m.hexdigest()


def findAnswer(c, amount):
    zeros = ["0"] * amount
    stringzeros = "".join(map(str, zeros))
    count = 0
    found = False
    while not found:
        n = getHash(c, count)
        if (n[:amount] == stringzeros):
            found = True
        else:
            count += 1

    print(count)


findAnswer(content, 5)
findAnswer(content, 6)
