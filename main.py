N = int(input("Введи количество простых чисел"))


prost_mas = [i if i != 1 else 0 for i in range(N + 1)]
i = 2
while i <= N:
    if prost_mas[i] != 0:
        j = i * 2
        while j <= N:
            prost_mas[j] = 0
            j += i
    i += 1
    
print(prost_mas)