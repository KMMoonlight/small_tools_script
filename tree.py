
#!/usr/bin/env python3
import os

path = os.getcwd()

def printTreeDoc(path, level):
    files = os.listdir(path)
    for item in files:
        print(printHor(level)+ "|-" + item)
        if os.path.isdir(path + "/" + item):
            printTreeDoc(path + "/" + item, level+1)


def printHor(level):
    hor = ""
    for x in range(0, level+1):
        hor += " "
    return hor


if __name__ == "__main__":
    printTreeDoc(path, 0)
