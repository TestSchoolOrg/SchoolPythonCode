n = 2 * 2187**2020 + 729**2021 - 2 * 243**2022 + 81**2023 - 2 * 27**2024 - 6561

def decToX(n, x):
    result = []
    while n != 0:
        result.append(n % x)
        n //= x
    return result[::-1]

x = decToX(n, 25)
count = sum(1 for d in x if d > 9)
print(count)
