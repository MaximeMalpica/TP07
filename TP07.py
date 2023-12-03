"""Class representing a ValueZero exception"""
class ValueZero(Exception):
    pass

class Fraction:
    """Class representing a fraction and operations on it

    Author : M. Malpica Arana
    Date : 01/12/2023
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """Initialize a Fraction object with a numerator and denominator.

        PRE : Les paramètres num et den doivent être des entiers.
            Le dénominateur (den) ne doit pas être égal à zéro.
        POST : Initialise un objet Fraction avec le numérateur et le dénominateur donnés.
        """

        self.__numerator = ""
        self.__denominator = ""

        try:
            if type(den) == str or type(den) == str:
                raise TypeError
            
            elif den == 0:
                raise ValueZero("le dénominateur doit etre différent de 0")
            
            self.__numerator = num
            self.__denominator = den

        except ValueZero as e:
            print(e)

        except TypeError:
            print("mauvais type de donnée saisie")


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
        RAISES : ValueError si num n'est pas un int ou une fraction.
        """

        if isinstance(num, int):
            num = Fraction(num)
        if not isinstance(num, Fraction):
            raise ValueError("Doit être un int ou une fraction")
        return num

# ------------------ Textual representations ------------------

    def __str__(self) :
        """Return a textual representation of the reduced form of the fraction

        POST : Renvoie la valeur du numérateur et du dénominateur séparés par / 
        """
        return f'{self.__numerator}/{self.__denominator}'


    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number.
        A mixed number is the sum of an integer and a proper fraction

        POST : Renvoie la valeur int de la fraction et le reste de la fraction séparé par des +.
        """

        int_value = self.numerator // self.denominator
        fraction_value = Fraction(self.numerator % self.denominator, self.denominator)
        return f'{int_value} + {fraction_value}'

   # ------------------ Operators overloading ------------------

    def __add__(self, other:int):
        """Overloading of the + operator for fractions.

        PRE : Une valeur numérique.
        POST : Renvoie l'addition de 2 éléments.
        RAISES : TypeError si other n'est pas additionnable.
        """
        other = self.is_fraction(other)
        add_num = self.numerator * other.denominator + self.denominator * other.numerator
        add_den = self.denominator * other.denominator
        return Fraction(add_num, add_den)


    def __sub__(self, other:int):
        """Overloading of the - operator for fractions.

        PRE: Une valeur numérique.
        POST: Renvoie la soustraction de 2 éléments.
        """
        other = self.is_fraction(other)
        sub_num = self.numerator * other.denominator - self.denominator * other.numerator
        sub_den = self.denominator * other.denominator
        return Fraction(sub_num, sub_den)


    def __mul__(self, other:int):
        """Overloading of the * operator for fractions.

        PRE: Une valeur numérique.
        POST: Renvoie la multiplication de 2 éléments.
        """
        other = self.is_fraction(other)
        mul_num = self.numerator * other.numerator
        mul_den = self.denominator * other.denominator
        return Fraction(mul_num, mul_den)


    def __truediv__(self, other :int):
        """Overloading of the / operator for fractions.

        PRE : Une valeur numérique.
        POST : Renvoie la division de 2 éléments.
        """
        other = self.is_fraction(other)
        div_num = self.numerator * other.denominator
        div_den = self.denominator * other.numerator
        return Fraction(div_num, div_den)


    def __pow__(self, other: int):
        """Overloading of the ** operator for fractions.

        PRE: Un integer.
        POST: Renvoie la fraction élevé a la puissance de other.
        RAISES : TypeError si other n'est pas un nombre entier.
        """

        if not isinstance(other, int):
            raise TypeError('Doit être un nombre entier')

        pow_num = self.numerator ** other
        pow_den = self.denominator ** other
        return Fraction(pow_num, pow_den)

    
    def __eq__(self, other:int) -> bool:
        """Overloading of the == operator for fractions.

        PRE: Un integer.
        POST: Renvoie l'égalité entre deux fractions.
        """
        other = self.is_fraction(other)
        return float(self) == float(other)

    
    def __float__(self) -> float:
        """Returns the decimal value of the fraction.

        POST: Renvoie la valeur décimal de la fraction.
        """
        return self.numerator / self.denominator
    
# TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0.

        POST : Renvoie True si la fraction est 0 sinon False.
        """
        return not self.numerator


    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...).

        POST : Renvoie True si la fraction est un integer sinon False.
        """
        return self.denominator == 1


    def is_proper(self):
        """Check if the absolute value of the fraction is < 1.

        POST : Renvoie True si la valeur de la fraction est < 1 sinon False.
        """
        return abs(float(self)) < 1


    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form.

        POST : Renvoie True si la valeur du numérateur de la fraction est 1 sinon False.
        """
        return self.numerator == 1


    def is_adjacent_to(self, other) :
        """Check if two fractions differ by a unit fraction
        Two fractions are adjacents if the absolute value of the difference them is a unit fraction.

        PRE : Une fraction.
        POST : Renvoie True si deux fractions sont adjacentes sinon False.
        """
        return abs(self - other).is_unit()


tst =  Fraction(10,1)
print(tst)
print(tst.as_mixed_number())
print(tst.is_zero())
print(tst.is_integer())
print(tst.is_proper())
print(tst.is_unit())
