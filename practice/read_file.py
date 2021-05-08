import sys
import os
def print_args(args):
    try:
        with open('text.txt') as file:
            for line in file:
                print(line)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print_args(sys.argv)