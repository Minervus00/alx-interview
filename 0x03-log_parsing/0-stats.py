#!/usr/bin/python3
"""log parsing"""
import re
import signal


def parse_line(line, file_size):
    """Records code and file size if the line has the good format"""
    pattern = r"^(([0-9]{1,3}\.){3}[0-9]{1,3}) - "
    pattern += r"\[[0-9]{4}(-[0-9]{2}){2} ([0-9]{2}:){2}[0-9]{2}\.[0-9]{6}\] "
    pattern += r"\"GET /projects/260 HTTP/1\.1\" ([0-5]{3}) (\d+)$"
    # print(pattern)

    res = re.fullmatch(pattern, line)
    if not res:
        # print("no_good")
        return

    code = res.group(5)
    size = int(res.group(6))
    # print(code)
    # print(size)
    status[code] += 1
    file_size += size
    return file_size


def print_records():
    """Prints the records in the required format"""
    print("File size: {}".format(file_size))
    for code, val in status.items():
        print("{}: {}".format(code, val))


def signal_handler(signum, frame):
    """Handles ctrl-c command"""
    print_records()
    # raise KeyboardInterrupt


if __name__ == "__main__":
    status = dict(
        (val, 0) for val in [
            '200', '301', '400', '401', '403', '404', '405', '500'
        ]
    )

    file_size = 0

    signal.signal(signal.SIGINT, signal_handler)

    itr = 0
    while True:
        line = input()
        # print(line)
        res = parse_line(line, file_size)
        if res:
            itr += 1
            file_size = res

        if itr == 10:
            itr = 0
            print_records()
