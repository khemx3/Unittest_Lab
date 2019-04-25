class InvalidArgument(Exception): pass

def toHex(n):
    if type(n) != int:
        raise InvalidArgument('Not an integer')
    elif n <= 0:
        raise InvalidArgument("Not a positve integer")
    return (hex(n)[2:]).upper()

print(toHex(10))