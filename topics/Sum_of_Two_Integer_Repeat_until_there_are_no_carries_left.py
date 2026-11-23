def get_sum(a, b):
    mask = 0xFFFFFFFF          # keep numbers within 32 bits
    max_int = 0x7FFFFFFF       # largest positive 32-bit int

    while b != 0:
        carry = ((a & b) << 1) & mask
        a = (a ^ b) & mask
        b = carry

    # if a is above max_int, it represents a negative number
    return a if a <= max_int else ~(a ^ mask)


print(get_sum(1, 2))     # 3
print(get_sum(5, 3))     # 8
print(get_sum(-2, 3))    # 1
