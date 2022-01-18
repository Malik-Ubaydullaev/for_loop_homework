def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    idx = 0
    list2 = []
    for i in list1:
         list2.append(list1[idx].capitalize())
         idx += 1
    return list2