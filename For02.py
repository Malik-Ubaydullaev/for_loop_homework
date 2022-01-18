def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    list1 = []
    for i in range(n):
        list1.append(i)
    stroka = str(list1)
    return stroka[1:-1]