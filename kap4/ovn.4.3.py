lön = 0.01 #startlön
ggr = 0 #de antal gånger man dubblar lönen
dag = 1 #antal dagar det tar att tjäna tot 10 000 000kr
tot = 0 #vad man haar tjänat totalt

print(f'dag 0 har man tjänat 0 kr') #skriver ut hur många dagar man tjänat dag 0

while tot < 10000000: #medans totalen av hur mycket man tjänat är mindre än 10 miljoner så kommer den att fortsätta loopa
    print(f'dag {dag:.0f} har man tjänat {tot:.2f} kr') #skriver ut efter varje loop vilken dag man är på och hur mycket man tjänar
    tot = tot + lön #adderar de man tjänat totalt med sin nuvarande lön
    lön = lön + lön #man dubblar lönen
    ggr = ggr + 1 #hur många gågner loopen har körts
    dag = dag + 1 #hurmånga dagar de gått
    print(f'Du har totalt tjänat {tot:.2f} kr') #skriver ut total summan man tjänat från dag 1

print(f'Det tog {ggr} dagar att tjäna {tot} kr') #skriver ut hur många dagar det tog att tjäna ihop 10 miljoner


