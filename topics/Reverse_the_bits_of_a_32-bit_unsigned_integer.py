def reverse_bits(n):
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)   # shift result left, append n's last bit
        n >>= 1                            # drop n's last bit
    return result

print(reverse_bits(43261596))   # 964176192
