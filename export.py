#! /usr/bin/env python -u
# coding=utf-8
import json

__author__ = 'xl'

header_line = "#EXTM3U\n"
record_line = "#EXTINF:%d,%s\n%s\n"


def generate(input_file, output_file):
    ret = header_line
    with open(input_file, "r") as fp:
        data = json.load(fp)

    for index, record in enumerate(data):
        title = record['title'] if 'title' in record else ''
        title = title[0] if type(title) is list else title
        ret += record_line % (index, title, record['video_url'])

    with open(output_file, "wb") as fp:
        fp.write(ret)


if __name__ == "__main__":
    generate("data.json", "Iranian Channels.m3u")
    generate("movies/movies.json", "Movies.m3u")

