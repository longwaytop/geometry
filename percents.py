

def percents(x, y):
    """ what percent of x is y"""
    one_precent = x / 100
    result = y / one_precent
    print(str(y) + " is " + str(result) + " % of " + str(x))
    return result


def print_percents(x, y):
    """Print what percent of x is y"""
    print(str(y) + " is " + str(result) + " % of " + str(x))


percents(200, 50)