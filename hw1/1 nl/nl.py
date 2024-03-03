import sys


def nl_file(filename):
    input_file = open(filename, mode='r')
    lines = input_file.readlines()

    i = 0
    for line in lines:
        line = line.replace('\n', '').replace('\r', '')
        if line != '':
            i += 1
            print(i, line)
        else:
            print('')


def nl_stdin():
    i = 1
    for line in sys.stdin:
        print(i, line, end='')
        i += 1


def run():
    if len(sys.argv) == 1:
        nl_stdin()
        return
    nl_file(sys.argv[1])


if __name__ == '__main__':
    run()
