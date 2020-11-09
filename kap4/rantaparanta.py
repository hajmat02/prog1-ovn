# ränta på ränta

balance = float(input("ditt starkapital: "))
save = float(input("jag vill spara i månaden: "))
year = int(input("under hur många år: "))
interest = int(input("ränta i %: "))
balanceWithInterest = balance
balance = 0

for i in range(1, year):
    balance += save * 12
    balanceWithInterest += save * 12
    balanceWithInterest *= (interest / 100 + 1)
    print(f"efter år {i} har du sparat {balance:.2f}, vilket är {balanceWithInterest:.2f} kronor")