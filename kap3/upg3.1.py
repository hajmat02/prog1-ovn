m = float(input('Hur många minuter har du ringt denna månad? '))
k = float(input('Hur mycket kostar varje minut? '))
pris = m+k
if  pris > 300:
    pris = pris * 0.9
print(f'Pris: {pris:.2f}')
