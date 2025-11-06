from string import ascii_lowercase
alph = "0123456789" + ascii_lowercase

for x in alph:
    w1 = int('923' + x + '874', 29)
    w2 = int('524' + x + '6152', 29)
    if (w1 + w2) % 28 == 0:
        print(x, (w1 + w2) // 28)
