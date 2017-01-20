from math import pow


class complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __add__(self, other):
        return complex(self.real + other.real, self.image + other.imag)

    def __sub__(self, other):
        return complex(self.real - other.real, self.image - other.imag)

    def __mul__(self, other):
        return complex(self.real * other.real - self.image * other.imag, self.real * other.imag + self.image * other.real)

    def __div__(self, other):
        try:
            return self.__mul__(complex(other.real, -1 * other.imag)).__mul__(complex(1.0 / (other.mod().real) ** 2, 0))
        except ZeroDivisionError as e:
            print(e)
            return None

    def mod(self):
        return complex(pow(self.real ** 2 + self.image ** 2, 0.5), 0)

    def __str__(self, precision=2):
        return str(("%." + "%df" % precision) % float(self.real)) + ('+' if self.image >= 0 else '-') + str(
            ("%." + "%df" % precision) % float(abs(self.image))) + 'i'


A = complex(*map(float, input().strip().split()))
B = complex(*map(float, input().strip().split()))

print(A + B)
print(A - B)
print(A * B)
print(A / B)
print(A.mod())
print(B.mod())
