s = input('Skriv en text: ')
i = 0
for c in s:
    if c == ' ' or c == '\t':
        break
    i = i + 1
if i < len(s):
    print(f'Första vita tecknet finns på plats nr {i}')
else:
    print('Inget vitt tecken')