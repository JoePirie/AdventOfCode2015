f = open("Input.txt", "r")
content = f.read()


def getCoord(n):
    try:
        coordB = n.split(" ")[4]
        coordA = n.split(" ")[2]
        command = n.split(" ")[1]
    except:
        coordA = n.split(" ")[1]
        coordA.split(",")
        coordB = n.split(" ")[3]
        command = n.split(" ")[0]

    return coordA.split(","), coordB.split(","), command


def partOne(c):
    strings = c.split("\n")
    array = []
    for i in range(0, 1000):
        n = []
        for i in range(0, 1000):
            n.append("off")
        array.append(n)

    for i in strings:
        coordA, coordB, command = getCoord(i)
        differenceX = int(coordB[0]) - int(coordA[0])
        differenceY = int(coordB[1]) - int(coordA[1])

        if command == "toggle":
            for y in range(0, differenceY + 1):
                for x in range(0, differenceX + 1):
                    value = array[int(coordA[1]) + y][int(coordA[0]) + x]
                    if value == "on":
                        array[int(coordA[1]) + y][int(coordA[0]) + x] = "off"
                    else:
                        array[int(coordA[1]) + y][int(coordA[0]) + x] = "on"
        else:
            for y in range(0, differenceY + 1):
                for x in range(0, differenceX + 1):
                    array[int(coordA[1]) + y][int(coordA[0]) + x] = command

    count = 0
    for i in array:
        for j in i:
            if j == "on":
                count += 1

    print(count)


def partTwo(c):
    strings = c.split("\n")
    array = []
    for i in range(0, 1000):
        n = []
        for i in range(0, 1000):
            n.append(0)
        array.append(n)

    for i in strings:
        coordA, coordB, command = getCoord(i)
        differenceX = int(coordB[0]) - int(coordA[0])
        differenceY = int(coordB[1]) - int(coordA[1])

        if command == "toggle":
            for y in range(0, differenceY + 1):
                for x in range(0, differenceX + 1):
                    array[int(coordA[1]) + y][int(coordA[0]) + x] = (array[int(coordA[1]) + y][int(coordA[0]) + x]) + 2

        elif command == "on":
            for y in range(0, differenceY + 1):
                for x in range(0, differenceX + 1):
                    array[int(coordA[1]) + y][int(coordA[0]) + x] = (array[int(coordA[1]) + y][int(coordA[0]) + x]) + 1
        else:
            for y in range(0, differenceY + 1):
                for x in range(0, differenceX + 1):
                    if (array[int(coordA[1]) + y][int(coordA[0]) + x]) - 1 < 0:
                        (array[int(coordA[1]) + y][int(coordA[0]) + x]) = 0
                    else:
                        array[int(coordA[1]) + y][int(coordA[0]) + x] = (array[int(coordA[1]) + y][int(coordA[0]) + x]) - 1

    count = 0
    for i in array:
        for j in i:
            count += j

    print(count)


#partOne(content)
partTwo(content)
f.close()
