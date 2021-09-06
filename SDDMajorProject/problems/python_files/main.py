from os import sys

def func (a):
    return 2 * a

if __name__ == "__main__":
    print(func(int(sys.argv[1])))