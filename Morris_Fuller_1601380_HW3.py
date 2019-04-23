def TheRoundTrip(dirs):
    valid_input = ["U", "D", "L", "R"]
    vertical = 0
    horizontal = 0
    count = 0
    for i in dirs:
        for j in valid_input:
            if i == j:
                count += 1
                for k in dirs:
                    if k == "U":
                        vertical += 1
                    elif k == "D":
                        vertical -= 1
                    elif k == "R":
                        horizontal += 1
                    else:
                        horizontal -= 1
            else:
                continue
    if count != len(dirs):
        print("bad input")
    else:
        if vertical == 0 and horizontal == 0:
            print(True)
        else:
            print(False)


TheRoundTrip(["U", "U", "R", "L", "D"])



