#!/usr/bin/python3
import sys


def print_msg(dict_sc, total_file_size):
    """
    Print: total file size and the count of each status code.
    """
    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
counter = 0
dict_sc = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # Split the line by spaces
        if len(parsed_line) < 7:  # Ensure the line has at least 7 components
            continue

        # Extract the file size and status code from the parsed line
        file_size = int(parsed_line[-1])
        status_code = parsed_line[-2]

        total_file_size += file_size  # Add to total file size
        counter += 1

        if status_code in dict_sc:
            dict_sc[status_code] += 1  # Increment status code count

        if counter == 10:
            print_msg(dict_sc, total_file_size)  # Print every 10 lines
            counter = 0

finally:
    print_msg(dict_sc, total_file_size)  # Print all input is processed
