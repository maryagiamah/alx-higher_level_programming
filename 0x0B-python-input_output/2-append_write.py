#!/usr/bin/python3
""" A modlue containing  write_file func """


def append_write(filename="", text=''):
    ''' Writes to a file by appendind to it'''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
