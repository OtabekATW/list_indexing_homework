def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
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
            list2 += [True]
        i += 1

    return list2