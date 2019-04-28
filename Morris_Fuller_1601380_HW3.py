# Position queries takes in the list of data, and the list of the desired sequence of values to extract. If the order is
# longer than the data, either list has 0 length, or if one isn't a list, it throws an error. If these are all met, it
# iterates through the order list and appends to an empty list "output" each value of order, minus one, which
# corresponds to the relevant zero-based index in data. It then returns the list "output".
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
    return output


# Round trip takes the list of directions and checks it against a list of valid directions. it there is a match, a
# a counter is added to later verify if the directions are all valid. The match is then added to or subtracted from
# a counter vertical or horizontal. Once the iteration is done, the function checks if the counter of matched directions
# matches the length of the list of directions, which verifies all the values in the input are valid. If it is less,
# it throws an error. It is is the same, it returns True if vertical and horizontal are both zero, meaning the
# directions returned to the origin, and False if either isn't zero.
def theRoundTrip(dirs):
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
        return "bad input"
    else:
        if vertical == 0 and horizontal == 0:
            return True
        else:
            return False


# Secret key takes the input of the list of keys and the required sum. It uses a nested for loop to iterate through
# the list of keys and a copy of the list. Ignoring duplicates, to make sure it doesn't add a key to itself, it checks
# if the sum of every value to every other is equal to the required sum. If it is, it adds to a counter. Once the
# iteration is finished, if the counter is above zero, there is at least one permutation that is correct, and True is
# returned. If there are no correct sums, False is returned.
def isSecretKey(key_ring, secret_key):
    count = 0
    key_ring2 = key_ring
    for i in key_ring:
        for j in key_ring2:
            if j != i and i + j == secret_key:
                count += 1
    if count > 0:
        return True
    else:
        return False


# Alien language, and the sub function alien word determine if a sentence is constructed entirely of palindromes or not.
# The alien word function acts recursively, checking if the first and last letters of a string are the same. If they
# are, it calls itself again on a the same string, less the first and last letters. The function returns false if the
# first and last letters aren't the same, and returns True if the length of the word is less than one, meaning the
# word has been iterated through and no discrepancies have been found.  The outer alien language function takes a
# sentence and iterates through it, calling isAlienWord on every word and adding to a counter if it returns True. If
# the counter is the same as the length of the sentence in words, the function is in an alien language and True is
# returned. Otherwise, False is returned.
def isAlienLanguage(sentence):
    def isAlienWord(word):
        if len(word) < 1:
            return True
        else:
            if word[0] == word[-1]:
                return isAlienWord(word[1:-1])
            else:
                return False
    count = 0
    sentence = sentence.split(" ")
    for word in sentence:
        if isAlienWord(word):
            count += 1
    if count == len(sentence):
        return True
    else:
        return False


def main():
    results = list()
    results.append(positionQueries([1, 2, 5, 0, 3], [1, 2]))
    results.append(theRoundTrip(["U", "R", "L", "D"]))
    results.append(isSecretKey([1, 2, 6, 7, 9], 3))
    results.append(isAlienLanguage("aabbbbaa mom"))
    for i in results:
        print(i)


if __name__ == '__main__':
    main()
