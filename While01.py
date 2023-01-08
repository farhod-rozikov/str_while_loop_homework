def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i, c = 0, 0
    while i < len(s):
        if s[i].isdigit():
            c += 1
        i += 1
    return c