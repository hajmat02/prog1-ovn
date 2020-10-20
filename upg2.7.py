import math #gör så att man kan skriva mattematiska saker på ett enkelt sätt

#ett program som räknar ut en cirkels area och omkrets 
svar = input ('Cirkelns radie:') 
r = float(svar) 
a = r*r * math.pi #räknar ut arean på cirkeln
b = (r+r) * math.pi #räknar ut omkretsen på cirkeln
print(f'Cirkelns area är:{a:.3f}')
print(f'Cirkelns omkrets är:{b:.3f}')