# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Performs division with robust error handling."""
    try:
        # Attempt to convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Try performing the division
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        # Handles non-numeric inputs
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        # Handles division by zero
        return "Error: Cannot divide by zero."

