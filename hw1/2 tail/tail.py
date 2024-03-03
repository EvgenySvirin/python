import sys


def tail_file(filename):
    input_file = open(filename, mode='r')
    lines = input_file.readlines()

    tail_index = max(0, len(lines) - 10)
    for line in lines[tail_index:]:
        print(line, end="")


def tail_stdin():
    lines = sys.stdin.readlines()

    tail_index = max(0, len(lines) - 10)
    for line in lines[tail_index:]:
        print(line, end="")


def print_filename_unix_tail(filename):
    print("==>", filename, "<==")


def run():
    if len(sys.argv) == 1:
        tail_stdin()
        return

    if len(sys.argv) == 2:
        tail_file(sys.argv[1])
        return

    filenames = sys.argv[1:]
    for filename in filenames:
        print("")
        if 1 < len(filenames):
            print_filename_unix_tail(filename)
        tail_file(filename)


if __name__ == '__main__':
    run()
