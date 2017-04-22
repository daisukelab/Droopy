#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

def do_my_process(output_directory='./processed', input_files=[]):
    '''Your own process'''
    # -- Exsample process #1, convert all the letters to upper case.
    command_line = 'awk \'{print toupper($0)}\' ' + ' '.join(input_files) + ' > ' + output_directory + '/test_upper.txt'
    print command_line

    # -- Exsample process #2, zip all to test.zip.
    #command_line = 'zip ' + output_directory + '/test.zip ' + ' '.join(input_files)
    #print command_line

    os.system(command_line)

if __name__ == '__main__':
    # -- Local test
    do_my_process(input_files=['Readme.md'])
