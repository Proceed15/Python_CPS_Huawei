N = int(input('Digite a quantidade: '))
L = []
for i in range(N):
    X = float(input(f'  elemento {i}: '))
    L.append(X)
print('\nResultado:')
for valor in L:
    print(f'  {valor:.3f}')
print('Fim do Programa')