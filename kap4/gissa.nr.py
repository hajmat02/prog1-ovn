import random

gissa = 0
random = random.randint(1,100)
gissningar = 0

while gissa != random:
    gissningar += 1
    gissa = int(input("gissa på ett heltal mellan 1 och 100: "))
    if gissa < random:
        print(f"fel, {gissa} är för litet, försök igen")
    elif gissa > random:
        print(f"fel, {gissa} är för stort, försök igen")
#if gissa == random:
print(f"Grattis, {gissa} är rätt")

print(f"Du behövde gissa {gissningar} gånger för att få rätt")

