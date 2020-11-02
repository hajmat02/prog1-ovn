y = float(input('Hur mycket kostar ett årskort? '))
b = float(input('Hur mycket kostar en biljett? '))
p = float(input('Hur många gånger tänker du besöka gymmet under ett år? '))
svar = p*b

if  svar>y:
    print('Ett årskort är bäst för dig.')
else:
    print('Att köpa biljetter är bäst för dig.')