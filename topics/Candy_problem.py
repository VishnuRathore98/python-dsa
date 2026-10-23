def candy(ratings):
    n = len(ratings)
    candies = [1] * n   # everyone starts with 1

    # left to right pass: handle increasing ratings
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # right to left pass: handle decreasing ratings
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)


ratings = [1, 0, 2]
print(candy(ratings))   # 5 -> candies = [2,1,2]

ratings2 = [1, 2, 2]
print(candy(ratings2))  # 4 -> candies = [1,2,1]
