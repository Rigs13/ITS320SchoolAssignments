import math

# CTA 6 for a Real/Imaginary number calculator
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        # Enter Code here
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return Complex(real, imaginary)
    
    def __sub__(self, other):
        # Enter Code here
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return Complex(real, imaginary)
    
    def __mul__(self, other):
        # Enter Code here
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real, imaginary)
    
    def __truediv__(self, other):
        # Enter Code here
        denom = other.real**2 + other.imaginary**2
        real = (self.real * other.real + self.imaginary * other.imaginary) / denom
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denom
        return Complex(real, imaginary)
    
    def mod(self):
        # Enter Code here
        real = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(real, 0)
    
    def __str__(self):
        # Enter Code here
        result = f"{self.real} + {self.imaginary}i"
        return result

def main():
    # Explaination of input
    print('Enter a real and imaginary number separated with a space below:')
    # First Input
    C = map(float, input().split())
    # Explanation of Second Input
    print('Enter a real and imaginary number separated with a space below:')
    # Second Input
    D = map(float, input().split())
    # Convert input to complex object using the Complex class
    x = Complex(*C)
    y = Complex(*D)

    print('\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()])))

if __name__ == "__main__":
    main()