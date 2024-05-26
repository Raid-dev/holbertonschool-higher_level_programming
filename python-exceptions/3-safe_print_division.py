#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        inside_res = a / b
    except ZeroDivisionError:
        inside_res = None
    finally:
        print("Inside result: {}".format(inside_res))
        return inside_res
