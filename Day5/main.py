f = open("Input.txt", "r")
content = f.read()


def checkUnallowedStrings(n):
    values = ["ab", "cd", "pq", "xy"]

    for i in values:
        if i in n:
            return True

    return False


def checkDoubledLetters(n):
    chars = list(n)
    currentstring = ""
    for i in chars:
        if i == currentstring:
            return True
        else:
            currentstring = i

    return False


def checkVowelCount(n):
    counter = 0
    for i in n:
        if str(i) in "aeiou":
            counter += 1

    if counter >= 3:
        return True
    else:
        return False


def checkPairs(n):
    prevChar = ""
    earlierChar = ""
    pairs = set()
    for char in n:
        if prevChar+char in pairs:
            return True
        if earlierChar != "":
            pairs.add(earlierChar+prevChar)
        earlierChar = prevChar
        prevChar = char
    return False




def checkRepeatedChar(n):
    nlist = list(n)
    x = True
    found = False
    counter = 0
    while x == True:
        try:
            currentChar = nlist[counter]
            if currentChar == nlist[counter + 2]:
                found = True
                x = False
            else:
                counter += 1
        except:
            x = False

    if found == False:
        return False
    else:
        return True


def partOne(c):
    strings = content.split("\n")
    count = 0
    for i in strings:
        if checkVowelCount(i) and checkDoubledLetters(i) and (not checkUnallowedStrings(i)):
            count += 1

    print(count)


def partTwo(c):
    strings = content.split("\n")
    count = 0
    for i in strings:
        if checkPairs(i) and checkRepeatedChar(i):
            count += 1

    print(count)


partOne(content)
partTwo(content)

f.close()
