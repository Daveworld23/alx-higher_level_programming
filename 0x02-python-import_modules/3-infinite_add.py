#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sumall = 0
    for i in range(1, len(argv)):
        sumall += int(argv[i])
    print("{}".format(sumall))
