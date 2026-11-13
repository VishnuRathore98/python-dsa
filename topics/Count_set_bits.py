def count_bits(n):
    count = 0
    while n:
        n &= (n - 1)   # removes the lowest set bit
        count += 1
    return count

print(count_bits(13))   # 3  (1101)
