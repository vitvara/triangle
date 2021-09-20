
def is_triangle(a: float, b: float, c: float) -> bool:
    """Test if the 3 numbers a, b, c can be the lengths of sides
    of a triangle.

    Arguments:
        a, b, c:  three positive numbers
    Returns:
        True if a, b, c can be lengths of sides of a triangle, False otherwise
    Raises:
        ValueError if any of a, b, c are not positive.
    """    

    if a < 0 or b < 0 or c < 0:
        raise ValueError("Arguments must be positive")

    if a >= b + c:
        return False
    if b >= a + c:
        return False
    if c > a + b:
        return False
    return True

