def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i, c = 0, 0
    while i < len(s):
        c += int(s[i])            
        i += 1
    return c