svar = input('Antal sekunder: ') #Läser in antalet sekunder från användaren
sek = int(svar) #Konverterar svaret till ett heltal
print('Inmatingen:', sek)
vecka = sek // 604800 #Delar antalet sekunder med antalet sekunder på en vecka, kapar till heltal med //
sek = sek % 604800 #Använder modulo för att räkna ut antalet sekunder som blev över från veckorna
print('Rest från veckor', sek)
dag = sek // 86400 #Delar antalet sekunder med antalet sekunder på en dag, kapar till heltal med //
sek = sek % 86400 #Använder modulo för att räkna ut antalet sekunder som blev över från dagarna
print('Rest från dagar', sek)
tim = sek // 3600 #Delar antalet sekunder med antalet sekunder på en timme, kapar till heltal med //
sek = sek % 3600 #Använder modulo för att räkna ut antalet sekunder som blev över från timmarna
print('Rest från timmar', sek)
min = sek // 60 #Delar antalet sekunder med antalet sekunder på en minut, kapar till heltal med //
sek = sek % 60 #Använder modulo för att räkna ut antalet sekunder som blir över från minutrarna
print('Rest från minuter:', sek)
print('Veckor', vecka)
print('Dagar:', dag)
print('Timmar:  ', tim)
print('Minuter: ', min)
print('Sekunder: ', sek)