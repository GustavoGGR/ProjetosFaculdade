Entrada = input().split()
A = float(Entrada[0])
B = float(Entrada[1])
if B % A == 0 or A % B == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
