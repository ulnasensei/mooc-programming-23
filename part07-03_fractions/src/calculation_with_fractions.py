def fractionate(amount: int):
    from fractions import Fraction

    return [Fraction(1, amount) for i in range(amount)]
