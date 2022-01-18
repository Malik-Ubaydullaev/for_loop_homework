def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    Sum = 0
    i = A
    for i in range(A,B):
        Sum += i
    return Sum