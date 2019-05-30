popA = 80000
txcreA = 1.03
popB = 200000
txcreB = 1.015
anospassados = 0
while popA <= popB:
    popA *= txcreA
    popB *= txcreB
    anospassados += 1
print(f'Serão necessários {anospassados} anos para que a população do país A ultrapasse a população do país B.')
