import sys
import os
def print_args(args):
    try:
        with open('text.txt') as file:
            for line in read_by_chunks(file):
                print(line)
    except Exception as e:
        print(e)

def read_by_chunks(file, chunk = 1024)
    while True:
        data = file.read(chunk)
        if not data:
             break
        yield data

if __name__ == "__main__":
    print_args(sys.argv)