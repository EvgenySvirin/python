import sys
import os


def wc_file(filename):
    lines_amount = 0
    words_amount = 0
    bytes_amount = 0

    input_file = open(filename, mode='r')
    file_stats = os.stat(filename)

    lines = input_file.readlines()

    for line in lines:
        words_amount += len(line.split())
        line = line.replace('\n', '').replace('\r', '')
        if len(line) != 0:
            lines_amount += 1

    bytes_amount = file_stats.st_size
    return lines_amount, words_amount, bytes_amount


def wc_stdin():
    lines_amount = 0
    words_amount = 0
    bytes_amount = 0

    symbols = sys.stdin.read()
    all_lines = symbols[:-1].split('\n')
    lines_amount = len(all_lines)

    for line in all_lines:
        words_amount += len(line.split())

    bytes_amount = len(symbols)
    return lines_amount, words_amount, bytes_amount


def run():
    if len(sys.argv) == 1:
        lines_amount, words_amount, bytes_amount = wc_stdin()
        print(lines_amount, words_amount, bytes_amount)
        return

    total_lines_amount = 0
    total_words_amount = 0
    total_bytes_amount = 0
    filenames = sys.argv[1:]
    for filename in filenames:
        lines_amount, words_amount, bytes_amount = wc_file(filename)
        print(' ', lines_amount, words_amount, bytes_amount, filename)
        total_lines_amount += lines_amount
        total_words_amount += words_amount
        total_bytes_amount += bytes_amount

    if 1 < len(filenames):
        print(' ', total_lines_amount, total_words_amount, total_bytes_amount, 'total')


if __name__ == '__main__':
    run()
