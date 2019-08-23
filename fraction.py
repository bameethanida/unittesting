from math import gcd

class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        if numerator == 0 and denominator == 0:
            self.numerator = 0
            self.denominator = 0
        # check type of numerator and denominator
        if not isinstance(numerator, int):
            raise TypeError("Numerator must be 'int' ")
        if not isinstance(denominator, int):
            raise TypeError("Denominator must be 'int' ")
        if isinstance(numerator, bool):
            raise TypeError("Numerator must be 'int' ")
        if isinstance(denominator, bool):
            raise TypeError("Denominator must be 'int' ")

        # infinity case (1/0), (-1/0)
        if denominator == 0:
            if numerator > 0:
                numerator = 1
            elif numerator < 0:
                numerator = -1
        # minus case
        elif denominator < 0:
            if numerator > 0:
                numerator = - numerator
            elif numerator < 0:
                numerator = abs(numerator)
            denominator = abs(denominator)
        # 0/0
        if numerator == 0 and denominator == 0:
            self.numerator = 0
            self.denominator = 0
        # Fractions are stored in proper form.
        else:
            self.gcd = gcd(numerator, denominator)
            self.numerator = int(numerator/self.gcd)
            self.denominator = int(denominator/self.gcd)

    def __str__(self):
        """Return the string in form of 'a/b' where a is numerator and b is denominator in proper form.
        """
        if self.numerator == 0 and self.denominator == 0:
            return '{0}/{1}'.format(self.numerator, self.denominator)
        if self.numerator == 0 or self.denominator == 1:
            return '{0}'.format(int(self.numerator/self.denominator))
        return '{0}/{1}'.format(self.numerator, self.denominator)
    
    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        new_num = self.numerator * frac.denominator + frac.numerator * self.denominator
        new_deno = self.denominator * frac.denominator
        return Fraction(new_num, new_deno)
    
    def __sub__(self, frac):
        """Return the subtraction of two fractions as a new fraction.
           Use the standard formula  a/b - c/d = (ad-bc)/(b*d)
        """
        new_num = self.numerator * frac.denominator - frac.numerator * self.denominator
        new_deno = self.denominator * frac.denominator
        return Fraction(new_num, new_deno)

    def __mul__(self, frac):
        """Return the multiplication of two fractions as a new fraction."""
        new_num = self.numerator * frac.numerator
        new_deno = self.denominator * frac.denominator
        return Fraction(new_num, new_deno)
    
    def __gt__(self, frac):
        """Return True if one fraction is greater than the other."""
        check_self = self.numerator * frac.denominator
        check_other_frac = frac.numerator * self.denominator
        return check_self > check_other_frac
    
    def __neg__(self):
        """Return negative value of fraction."""
        return Fraction(-self.numerator, self.denominator)
     
    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.numerator == frac.numerator and self.denominator == frac.denominator
