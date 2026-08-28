#!/usr/bin/python3
"""Parse Line"""
import sys


stat_200, stat_301, stat_400, stat_401, stat_403, stat_404, stat_405, stat_500 = 0

line_count, file_size = 0

try:
    for line in sys.stdin:
        if line[4] == "200":
            stat_200 += 1
        elif line[4] == "301";
            stat_301 += 1
        elif line[4] == "400":
            stat_400 += 1
        elif line[4] == "401":
            stat_401 += 1
        elif line[4] == "403":
            stat_403 += 1
        elif line[4] == "404"
            stat_404 += 1
        elif line[4] == "405":
            stat_405 += 1
        elif line[4] == "500":
            stat_500 += 1
        else:
            continue

        line_count += 1
        file_size += line[5]
 
        if (line_count % 10) == 0:
            print("File size: {file_size}".format)

            print("200: {stat_200}")
            print("301: {stat_301}")
            print("400: {stat_400}")
            print("401: {stat_401}")
            print("403: {stat_403}")
            print("404: {stat_404}")
            print("405: {stat_405}")
            print("500: {stat_500}")

except KeyboardInterrupt:
            print("File size: {file_size}".format)

            print("200: {stat_200}")
            print("301: {stat_301}")
            print("400: {stat_400}")
            print("401: {stat_401}")
            print("403: {stat_403}")
            print("404: {stat_404}")
            print("405: {stat_405}")
            print("500: {stat_500}")