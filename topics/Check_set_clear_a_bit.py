n = 5   # 101

print((n >> 1) & 1)    # 0  -> bit at position 1 is off
print(n | (1 << 1))    # 7  -> set bit 1
print(n & ~(1 << 0))   # 4  -> clear bit 0
