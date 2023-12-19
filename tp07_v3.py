"""Module to use math operations"""
import math

class Fraction:
    """Class representing a fraction and operations on it

    Author : M. Malpica Arana
    Date : 19/12/2023
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """Initialize a Fraction object with a numerator and denominator.

        PRE :
        - num : un int qui représente le numérateur d'une fraction
        - den : un int qui représente le dénominateur d'une fraction
        POST : Initialise un objet Fraction avec le numérateur et le dénominateur donnés.
        RAISES : ZeroDivisionError si den égal 0
        """
        if den == 0:
            raise ZeroDivisionError("Le dénominateur de la fraction ne peut pas être 0")

        abs_num = abs(num)
        if num / den < 0:
            num = -abs_num
        else:
            num = abs_num

        common_divisor = math.gcd(num, den)
        self.__numerator = num // common_divisor
        self.__denominator = abs(den) // common_divisor

    @property
    def numerator(self):
        """This gets the value of numerator.

        POST : Renvoie la valeur du numérateur.
        """
        return self.__numerator

    @property
    def denominator(self):
        """This gets the value of denominator.

        POST : Renvoie la valeur du dénominateur.
        """
        return self.__denominator
    @staticmethod
    def is_fraction(num: int):
        """A function to set a value to Fraction

        PRE : Une valeur numérique.
        POST : Renvoie la fraction de la valeur.
        RAISES : ValueError si num n'est pas un int ou une fraction
        """

        if isinstance(num, int):    #type d'un param
            num = Fraction(num)
        if not isinstance(num, Fraction):
            raise ValueError("Doit être un int ou une fraction")
        return num

# ------------------ Textual representations ------------------

    def __str__(self) :
        """Return a textual representation of the reduced form of the fraction

        POST : Renvoie un string contenant le numérateur et le dénominateur séparés par un '/'gg
        """
        return f'{self.__numerator}/{self.__denominator}'

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number.
        A mixed number is the sum of an integer and a proper fraction

        POST : Renvoie un string avec la valeur int de la fraction et 
            le reste de la fraction séparé par un '+'.
        """

        int_value = self.numerator // self.denominator
        fraction_value = Fraction(self.numerator % self.denominator, self.denominator)
        return f'{int_value} + {fraction_value}'

   # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions.

        PRE : 'other' est une instance de Fraction
        POST : Renvoie une nouvelle fraction représentant la somme des deux fractions
        """
        other = self.is_fraction(other)
        add_num = self.numerator * other.denominator + self.denominator * other.numerator
        add_den = self.denominator * other.denominator
        return Fraction(add_num, add_den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions.

        PRE: 'other' est une instance de Fraction
        POST: Renvoie une nouvelle fraction représentant la différence des deux fractions
        """
        other = self.is_fraction(other)
        sub_num = self.numerator * other.denominator - self.denominator * other.numerator
        sub_den = self.denominator * other.denominator
        return Fraction(sub_num, sub_den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE: 'other' est une instance de Fraction
        POST: Renvoie une nouvelle fraction représentant la multiplication des deux fractions
        """
        other = self.is_fraction(other)
        mul_num = self.numerator * other.numerator
        mul_den = self.denominator * other.denominator
        return Fraction(mul_num, mul_den)

    def __truediv__(self, other :int):
        """Overloading of the / operator for fractions.

        PRE : 'other' est une instance de Fraction 
        POST : Renvoie une nouvelle fraction représentant la division des deux fractions
        RAISES : ZeroDivisionError si 'denominator' est nul
        """

        if other.denominator == 0:
            raise ZeroDivisionError("La division par zéro n'est pas autorisée.")
        other = self.is_fraction(other)
        div_num = self.numerator * other.denominator
        div_den = self.denominator * other.numerator
        return Fraction(div_num, div_den)

    def __pow__(self, other: int):
        """Overloading of the ** operator for fractions.

        PRE: 'other ' est un entier
        POST: Renvoie une nouvelle fraction représentant la puissance de la fraction
        RAISES : TypeError si other n'est pas un nombre entier
        """

        if not isinstance(other, int):
            raise TypeError('Doit être un nombre entier')

        pow_num = self.numerator ** other
        pow_den = self.denominator ** other
        return Fraction(pow_num, pow_den)
    def __eq__(self, other:int) -> bool:
        """Overloading of the == operator for fractions.

        PRE: 'other' est une instance de Fraction
        POST: Renvoie True si les deux fractions sont équivalentes , False sinon
        """
        other = self.is_fraction(other)
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __float__(self) -> float:
        """Returns the decimal value of the fraction.

        POST: Renvoie la valeur décimale de la fraction
        """
        return self.numerator / self.denominator
#[BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0.

        POST : Renvoie True si la fraction est nulle, False sinon T = 1 F = 0
        """
        return not self.numerator

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...).

        POST : Renvoie True si la fraction est un entier, False sinon
        """
        return self.denominator == 1

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1.

        POST : Renvoie True si la fraction est propre, False sinon
        """
        return abs(float(self)) < 1

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form.

        POST : Renvoie True si le numérateur est 1, False sinon
        """
        return self.numerator == 1

    def is_adjacent_to(self, other)  :
        """Check if two fractions differ by a unit fraction
        Two fractions are adjacents if the absolute value of the difference them is a unit fraction.

        PRE : Une fraction.
        POST : Renvoie True si deux fractions sont adjacentes sinon False.
        """
        diff = abs(self.numerator * other.denominator - other.numerator * self.denominator)
        return diff == 1

def test_condition(fraction, adjacent):
    """Cette fonction permet d'afficher les différentes méthodes de conditions"""
    print("----------- TEST CONDITION METHODE ----------")
    print(f'- as_mixed_number(self) : {fraction.as_mixed_number()}')
    print(f'- is_zero(self): {fraction.is_zero()}')
    print(f'- is_integer(self) : {fraction.is_integer()}')
    print(f'- is_proper(self) : {fraction.is_proper()}')
    print(f'- is_unit(self) : {fraction.is_unit()}')
    print(f'- is_adjacent_to(self, other): {fraction.is_adjacent_to(adjacent)}\n')

def test_operation(fraction1, fraction2):
    """Cette fonction permet d'afficher les différentes méthodes d'opérations"""
    print("----------- TEST OPERATION METHODE ----------")
    print(f'- __add__(self,other) : {fraction1 + fraction2}')
    print(f'- __sub__(self,other) : {fraction1 - fraction2}')
    print(f'- __mul__(self,other) : {fraction1 * fraction2}')
    print(f'- __truediv__(self,other) : {fraction1 / fraction2}')
    print(f' - __eq__(self, other:int) : {fraction1 == fraction2}')
    print(f' - __float__(self) : {float(fraction1)}')
if __name__ == '__main__':
    try:
        frac = Fraction(3, 0)
        print(frac)
    except ZeroDivisionError as error:
        print(f'Error : \n---> {error}\n')

    test_condition(Fraction(10, 5), Fraction(9, 5))
    test_operation(Fraction(10, 5),Fraction(4, 3))
