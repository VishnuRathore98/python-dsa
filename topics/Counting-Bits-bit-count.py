def count_bits_simple(n):
    result = []
    for i in range(n + 1):
        count = 0
        x = i
        while x:
            x &= (x - 1)   # remove lowest set bit
            count += 1
        result.append(count)
    return result

print(count_bits_simple(5))   # [0, 1, 1, 2, 1, 2]
