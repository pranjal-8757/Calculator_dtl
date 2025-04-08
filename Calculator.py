# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def to_hex(n):
    return hex(n)

def from_hex(h):
    return int(h, 16)

def exponent(a, b):
    return a ** b



print("Addition:", add(2, 3))
print("Subtraction:", subtract(5, 2))
print("Decimal 255 to Hex:", to_hex(255))
print("Hex '0xff' to Decimal:", from_hex("0xff"))
print("Exponent:", exponent(3, 3))

