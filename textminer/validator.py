import re


def binary(x):
    return re.match(r'[0-1+]', x)

def binary_even(x):
    return re.match(r'[0-1]*0$', x)

def hex(x):
    return re.match(r'[^G-Z][\dA-F]+', x)

def word(x):
    return re.match(r'[\w/-]*[a-z]+$', x)
