f = open("input.txt", "r")
content = f.read()


def getDimensions(v):
    dimensions = list(map(int, v.split("x")))
    l = dimensions[0]
    w = dimensions[1]
    h = dimensions[2]
    organize = sorted(dimensions)

    return [l, w, h, organize]


def partOne(c):
    vals = c.split()
    paper = 0
    for i in vals:
        l, w, h, organize = getDimensions(i)

        paper += (2 * l * w) + (2 * w * h) + (2 * h * l) + (organize[0] * organize[1])

    print("The elves need " + str(paper) + " square feet of paper.")


def partTwo(c):
    vals = c.split()
    ribbon = 0
    for i in vals:
        l, w, h, organize = getDimensions(i)
        ribbon += (organize[0] * 2) + (organize[1] * 2) + (l * w * h)

    print("The elves need " + str(ribbon) + " feet of ribbon.")


partOne(content)
partTwo(content)

f.close()
