

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y

räknesätt = str(input('Välokmen till miniräknaren, välj ett av följande val [tyck enter för att fortsätta]'))
print('[1] Räkna med +')
print('[2] Räkna med -')
print('[3] Räkna med *')
print('[4] Avsluta')


while True:

    val = input('Välj vilket räknesätt du vill använda eller om du vill avsluta (1 , 2, 3, 4) ')
    if val in ('1', '2', '3', '4'):

        if val == '1':
            num1 = float(input("Vad är första nummret: "))
            num2 = float(input("Vad är  andra nummeret: "))
            print ('Summan av' , num1, '+', num2, '=', add (num1, num2))

else:
    print("Där hade du helt fel")