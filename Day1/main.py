f = open('input.txt', 'r')
content = f.read()


def checkVal(n, floors):
    if n == "(":
        floors += 1
    elif n == ")":
        floors -= 1
    else:
        print("error in checking character")

    return floors


def partOne(contents):
    vals = list(contents)
    floor = 0
    for i in vals:
        floor = checkVal(i, floor)

    print("Santa's floor is: " + str(floor))


def partTwo(contents):
    counter = 1
    vals = list(contents)
    floor = 0
    for i in vals:
        floor = checkVal(i, floor)

        if floor < 0:
            break
        else:
            counter += 1

    print("First Position to make Santa go into the basement is: " + str(counter))


partOne(content)
partTwo(content)

f.close()
