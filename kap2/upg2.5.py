pris=input('Skriv varans pris: ') #inmatning, konvertera till float
moms=input('Skriv varans moms i procent: ') #inmatning, konvertera till float

#räkna ut priset exklusive moms, pris delat i momsen omvandlat till decimal +1
emoms = pris / (moms / 100)

print(f'Priset exklusive moms: {emoms}')
print(f'Momsen är: {pris-moms}')