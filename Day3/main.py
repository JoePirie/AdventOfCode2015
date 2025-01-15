f = open("Input.txt", "r")
content = f.read()


def changeCoord(x, y, n):
    if n == ">":
        x += 1
    elif n == "<":
        x -= 1
    elif n == "^":
        y -= 1
    elif n == "v":
        y += 1
    else:
        print("error in checking val")

    return x, y


def partOne(c):
    locations = [[0, 0]]
    x = 0
    y = 0

    vals = list(c)
    for i in vals:
        x, y = changeCoord(x, y, i)

        coord = [x, y]
        if coord not in locations:
            locations.append(coord)

    print("The number of houses which get at least 1 present is: " + str(len(locations)))


def partTwo(c):
    locations = [[0, 0]]
    x = 0
    y = 0
    robox = 0
    roboy = 0
    counter = 1

    vals = list(c)
    for i in vals:
        if (counter % 2) == 0:
            robox, roboy = changeCoord(robox, roboy, i)
            coord = [robox, roboy]
        else:
            x, y = changeCoord(x, y, i)
            coord = [x, y]

        if coord not in locations:
            locations.append(coord)

        counter += 1

    print("The number of houses which get at least 1 present when robosanta is active is: " + str(len(locations)))


partOne(content)
partTwo(content)
f.close()
