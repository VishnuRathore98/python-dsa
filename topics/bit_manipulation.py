a, b = 5, 3        # 5 = 101, 3 = 011

print(a & b)       # 1   AND: 1 only if both bits are 1  (001)
print(a | b)       # 7   OR: 1 if either bit is 1        (111)
print(a ^ b)       # 6   XOR: 1 if bits differ           (110)
print(~a)          # -6  NOT: flips all bits
print(a << 1)      # 10  left shift: multiply by 2
print(a >> 1)      # 2   right shift: divide by 2
