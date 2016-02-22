import locale
import string
import sys


# global variables

# default symbols
currency_symbol = '$'
thousands_separator_symbol = ','
decimal_point_symbol = '.'


# global functions

def remove_symbols(s):
    """
    clear out the input string of currency and thousands separator symbols, but keep the decimal point
    """
    s = s.replace('\\\\', '\\') # replace double backslash with single
    s = s.replace('\n', ' ') # replace newlines with space
    s = s.replace('\r', ' ') # replace returns with space
    s = s.replace(currency_symbol, '') # remove curency symbol
    s = s.replace(thousands_separator_symbol, '') # remove thousands separator symbol
    if s[0] == '"' or s[0] == "'":
        s = eval(s) # quoted string - eval in case there are literal escaped characters
    elif string.find('\\', s):
        # no quotes but found a backslash - quote the string and eval
        s = '"' + s + '"'
        s = eval(s)
    return s


def sum_string(s):
    """
    sum the numbers in the string, separated by whitespace
    return float sum
    """
    return reduce(lambda x, y: x+y, map(float, string.split(s)))


# check the locale

if locale.setlocale(locale.LC_ALL, '') != 'C':
    # not the default C locale
    locale_conventions = locale.localeconv()
    currency_symbol = locale_conventions['currency_symbol']
    thousands_separator_symbol = locale_conventions['thousands_sep']
    decimal_point_symbol = locale_conventions['decimal_point']

print sum_string(remove_symbols(sys.stdin.read()))
