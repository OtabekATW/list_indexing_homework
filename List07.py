def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    list2 = []
    i = 0
    while i < len(list1):
        if list1[i] == 0:
            list2 += [False]
        else:
            list2 += [list1[i]]
        i += 1
    return list2