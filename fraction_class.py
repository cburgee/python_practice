##BROKEN
##TODO Need new variables for resulting addition and or multiplication.


class Fraction:
    def __init__(self, nr, dr=1):
        if dr == 0:
            raise ValueError("The denominator cannot be 0")
        elif dr < 0 and nr < 0:
            self.dr = dr * -1
            self.nr = nr * -1
        elif dr < 0 and nr >= 0:
            self.dr = dr * -1
            self.nr = nr * -1
        else:
            self.dr = dr
            self.nr = nr

    def multiply(self, multiplier):
        if isinstance(multiplier, int):
            self.nr = self.nr * multiplier
            self.dr = self.dr * multiplier
        else:
            self.nr = self.nr * multiplier.nr
            self.dr = self.dr * multiplier.dr
        result = Fraction(self.nr, self.dr)
        return result

    def add(self, addative):
        if isinstance(addative, int):
            self.nr = self.nr + (addative * self.dr)
        else:
            self.nr = (self.nr * addative.dr) + (addative.nr * self.dr)
            self.dr = self.dr * addative.dr
        result = Fraction(self.nr, self.dr)
        return result

    def show(self):
        print(f"{self.nr}/{self.dr}")


if __name__ == "__main__":
    f1 = Fraction(2, 3)
    f1.show()
    f2 = Fraction(3, 4)
    f2.show()
    f3 = f1.multiply(f2)
    f3.show()
    f3 = f1.add(f2)
    f3.show()
    f3 = f1.add(5)
    f3.show()
    f3.multiply(5)
    f3.show()
