#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        val = fct(*args)
        return val
    except Exception as err:
        print("Exception: {}". format(err), file=sys.stderr)
        return None
