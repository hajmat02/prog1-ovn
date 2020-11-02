import random

gissa = 0
random = random.randint(1,100)
while gissa != random:
    gissa = int(input("gissa på ett heltal mellan 1 och 100: "))
    if gissa < random:
        print(f"fel, {gissa} är för litet, försök igen")
    elif gissa > random:
        print(f"fel, {gissa} är för stort, försök igen")
if gissa == random:
    print(f"{gissa} är rätt")

