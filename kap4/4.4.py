sh = float(input('Start höjden i meter är:'))

cm = sh * 100
ggr = 0

while cm >= 1:
    cm = cm * 0.7
    print(f'{cm:.2f}')
    ggr = ggr + 1
print('bollen studsar' ,ggr)