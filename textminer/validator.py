import re


def binary(x):
    return re.match(r'[0-1+]', x)

def binary_even(x):
    return re.match(r'[0-1]*0$', x)

def hex(x):
    return re.match(r'[^G-Z][\dA-F]+', x)

def word(x):
    return re.match(r'[\w/-]*[a-z]+$', x)

def words(x, count=None):
    word_list = re.split('\s', x)
    if count:
        if count != len(word_list):
            return None
    if None in [re.match(r'[\w/-]*[a-z]+$', w) for w in word_list]:
        return None
    else:
        return word_list

def phone_number(x):
    return re.match(r'\(?(\d{3})\)?[-. ]?(\d{3})[-. ]?(\d{4})', x)

def money(x):
    return re.match(r'^[\$]{1}[\d]{1,3}(\,[\d]{3})*([\d]{3})*(\.[\d]{2})?$', x)

def zipcode(x):
    return re.match(r'[\d]{5}(\-[\d]{4})*$', x)

def date(x):
    return re.match(r'[\d]{,4}[/-][\d]{,4}[/-][\d]{,4}', x)
