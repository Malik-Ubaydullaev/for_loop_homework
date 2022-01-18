def main(A,B):
    """
    Return the numbers from A to B in the form of a list.
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
    return list1[A::]