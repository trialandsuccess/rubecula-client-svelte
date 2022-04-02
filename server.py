from rubecula import serve
import sys

from controllers import *


def main(*args):
    serve(args, dev=True)


if __name__ == '__main__':
    main(sys.argv[1:])
