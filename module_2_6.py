n = int(input("Введите число от 3 до 20: "))
result = []

for i in range(1, n):
    for j in range(i+1, n):
        if (i + j) % n == 0 or n % (i + j) == 0:
            result.append(i)
            result.append(j)

print(*result)
