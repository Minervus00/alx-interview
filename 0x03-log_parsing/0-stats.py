#!/usr/bin/python3
"""log parsing"""
import sys


def print_records(file_size, status):
    """Prints the records in the required format"""
    print("File size: {}".format(file_size))
    for code, val in status.items():
        print("{}: {}".format(code, val))


if __name__ == "__main__":
    status = dict(
        (val, 0) for val in [
            '200', '301', '400', '401', '403', '404', '405', '500'
        ]
    )

    file_size = 0

    try:
        itr = 0
        for line in sys.stdin:
            line = line.split()
            try:
                code = line[-2]
                if code in status:
                    status[code] += 1
                size = int(line[-1])
                file_size += size
            except Exception as ex:
                pass

            itr += 1
            if itr == 10:
                itr = 0
                print_records(file_size, status)

    except KeyboardInterrupt as kb:
        print_records(file_size, status)
        raise
    print_records(file_size, status)
