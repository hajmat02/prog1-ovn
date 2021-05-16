#Jag jobbade med Oskar och vi hjälpe varandra med olika problem vi hade 

def add(x, y):     #hitta detta på google för att de skulle vara lättare att skriva
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y

räknesätt = str(input('Välkommen till miniräknaren :) [tyck enter för att fortsätta]')) #välkomnande
print('[1] Räkna med +') 
print('[2] Räkna med -')
print('[3] Räkna med *')
print('[4] Avsluta')


while True:    #början av loopen

    val = input('Välj vilket räknesätt du vill använda eller om du vill avsluta [1 , 2, 3, 4] ') #här får du göra ditt val
    if val in ('1', '2', '3', '4'):

        if val == '1':    #ifall man valde 1
            num1 = float(input("Vad är första talet: ")) #frågar vad första talet är
            num2 = float(input("Vad är  andra talet: ")) #frågar vad andra talet är
            print ('Summan av' , num1, '+', num2, '=', add (num1, num2)) #räknar ut summan av num1 och num2 printar svaret
        elif val == '2':    #ifall man valde 2
            num1 = float(input("Vad är första talet: ")) #frågar vad första talet är
            num2 = float(input("Vad är  andra talet: ")) #frågar vad andra talet är
            print ('Differensen av', num1, '-', num2, '=', subtract (num1, num2)) #räknar ut differensen av num1 och num2 printar svaret
        elif val == '3':   #ifall man valde 3
            num1 = float(input("Vad är första talet: ")) #frågar vad första talet är
            num2 = float(input("Vad är andra talet: ")) #frågar vad andra talet är
            print ('Produkten av', num1, '*', num2, '=', multiply (num1, num2)) #räknar ut produkten av num1 och num2 printar svaret
        elif val == '4':   #ifall man valde 4
            print('Vad tråkigt att du inte ville räkna nå mer, hejdå :(') #avslutar programmet
            break
else:      #finns för att koden helt enkelt ska fungera
    print("Där hade du helt fel")
