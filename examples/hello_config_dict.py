#!/usr/bin/env python
# coding=utf-8
""" A configurable Hello World. Yay!

You can run it like this:
>>$ ./hello_config_dict.py
E   INFO - hello_config_dict - Running command 'main'
E   INFO - hello_config_dict - Started
    Hello world!
E   INFO - hello_config_dict - Completed after 0:00:00

"""
from __future__ import division, print_function, unicode_literals
from sacred import Experiment

ex = Experiment('hello_config_dict')


ex.add_config(
    message="Hello world!"
)


@ex.automain
def main(message):
    print(message)