a = 12
b = 3

print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a // b)   # 4 Divisão de números inteiros, arredondada para baixo em direção ao infinito negativo
print(a % b)    # 0 Módulo: o resto após a divisão de números inteiros

print("\nPrimeiro loop de 1 ate soma de a + b")
for i in range(1, a + b):
    print(i)

print("\nSegundo loop de b ate a")
for i in range(b, a):
    print(i)

