"""import numpy as np
lst = []

'''global a, b, c, d, e, f, g, h, i'''
a, b, c, d, e, f, g, h, i = 0, 0, 0, 0, 0, 0, 0, 0, 0

temBoard = {'Top-L': (' 5', a), 'Top-M': (' ', b), 'Top-R': (' ', c), 'Mid-L': (' ', d), 'Mid-M': (' ', e), 'Mid-R': (' ', f), 'Low-L': (' ', g),
            'Low-M': (' ', h), 'Low-R': (' ', i)}

if temBoard['Top-L'][1] == a:
    print('et')
tu = (14, 15)
temBoard['Top-L'][] = tu
print(temBoard['Top-L'])"""
a = input()
apple = 1
banana = 'f'
carrot = 3
fruitdict = {}
for i in ('apple', 'banana', 'carrot'):
    fruitdict[i] = locals()[i]
