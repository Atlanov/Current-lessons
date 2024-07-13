print("Всё не так уж просто")#Длинный вариант для наглядности
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(numbers)
primes = []
not_primes = []
is_prime = True
for i in range(1, len(numbers)):
    for j in range(1, i - 1):
        if numbers[i] % numbers[j] != 0:
            is_prime = True
            continue
        elif numbers[i] % numbers[j] == 0:
            is_prime = False
            not_primes.append(numbers[i])
        break
    if is_prime == True:
        primes.append(numbers[i])
print('Final Flag:', is_prime)
print('Primes:', primes)
print('Not Primes:', not_primes)
