def area(xmn1, ymn1, xmx1, ymx1, xmn2, ymn2, xmx2, ymx2):
    dx = min(xmx1, xmx2) - max(xmn1, xmn2)
    dy = min(ymx1, ymx2) - max(ymn1, ymn2)
    if (dx >= 0) and (dy >= 0):
        return dx * dy
    else:
        return False


if __name__ == "__main__":
    tests = (
        (1, 1, 2, 2, 3, 3, 4, 4),
        (1, 1, 6, 6, 3, 3, 4, 10),
        (0, 0, 3, 2, 0, 0, 5, 10),
    )
    for test in tests:
        print(area(*test))
