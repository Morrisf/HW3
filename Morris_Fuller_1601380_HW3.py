def positionQueries(data, order):
    if not type(data) or type(order) == "list":
        print("bad input: type")
        return
    elif len(data) == 0:
        print("bad input: zero")
        return
    elif len(order) == 0:
        print("bad input: zero")
    elif len(order) > len(data):
        print("bad input: length")
        return
    output = []
    for i in order:
        output.append(data[i-1])
    print(output)


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


def isSecretKey(key_ring, secret_key):
    count = 0
    key_ring2 = key_ring
    for i in key_ring:
        for j in key_ring2:
            if j != i and i + j == secret_key:
                count += 1
    if count > 0:
        print(True)
        return
    else:
        print(False)
        return


def isAlienWord(word):
    if len(word) < 1:
        return True
    else:
        if word[0] == word[-1]:
            return isAlienWord(word[1:-1])
        else:
            return False


def isAlienLanguage(sentence):
    count = 0
    sentence = sentence.split(" ")
    for word in sentence:
        if isAlienWord(word):
            count += 1
    if count == len(sentence):
        print(True)
    else:
        print(False)


isAlienLanguage("a ma")