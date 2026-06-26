
def careful_divide(a: float, b: float) -> float:
    """Divide a by b.
    Args:
        a:
        b:
    Returns:
    Raise:
        ValueError: When the inputs cannot be divided.
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs')



x, y = 5, 2
try:
    result = careful_divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)


