n = int(input("digite um número: "))

a, b = 0, 1

fibonacci = False

while a <= n:
    if a == n:
        fibonacci = True
        break
    a, b = b, a + b

if fibonacci:
    print(f"o número {n} pertence à sequência de Fibonacci.")
else:
    print(f"o número {n} não pertence à sequência de Fibonacci.")
