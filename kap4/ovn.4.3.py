lön = 0.01
ggr = 0
dag = 1
tot = 0

print(f'dag 0 får man 0 kr')

while tot < 10000000:
    print(f'dag {dag:.0f} har man tjänat totalt {tot:.2f} kr')
    tot = tot + lön
    lön = lön + lön
    ggr = ggr + 1
    dag = dag + 1
    print(f'Totalt tjänat {tot:.2f} kr')

print(f'Det tog {ggr} dagar att tjäna {tot} kr')


