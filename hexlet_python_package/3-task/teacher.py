def is_continuous_sequence(source):
    if len(source) < 2:
        return False
    for x, y in zip(source, source[1:]):
        if (y - x) != 1:
            return False
    return True