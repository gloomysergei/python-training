def chunked(size, source):
    result = []
    index = 0
    while index < len(source):
        result.append(source[index:index + size])
        index += size
    return result