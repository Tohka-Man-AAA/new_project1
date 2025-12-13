n = int(input())
a = [int(input()) for i in range(n)]

#сортировка
for i in range(3):
    for k in range(n - 1 - i):
        if a[k] > a[k + 1]:
            a[k], a[k + 1] = a[k + 1], a[k]

# Вывод
print(" ".join(map(str, a)) + " ")