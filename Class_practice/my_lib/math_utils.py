# my_lib/math_utils.py

class MathUtils:
    """A stateless utility class. 
    
    No __init__ needed because it doesn't track state.
    """

    @staticmethod
    def add(a: float, b: float) -> float:
        """Adds two numbers."""
        return a + b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiplies two numbers."""
        return a * b

    @staticmethod
    def is_positive(number: float) -> bool:
        """Checks if a number is greater than zero."""
        return number > 0