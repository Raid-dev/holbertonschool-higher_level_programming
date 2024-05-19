#!/usr/bin/python3
import sys

args = sys.argv
num_args = len(args)
summ = 0

if __name__ == "__main__":

    if num_args == 1:
        pass
    else:
        for i in range(1, num_args):
            summ += int(args[i])
    print("{}".format(summ))
