def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    list1 = []
    B += 1
    for i in range(B):
        list1.append(i) 
    n = B - A
    return list1[-1:-n-1:-1]