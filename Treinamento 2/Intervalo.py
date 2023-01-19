A = float(input())
if A < 0 or A > 100:
    print("Fora de intervalo")
if 0 <= A <= 25:
    print("Intervalo [0,25]")
if 25 < A <= 50:
    print("Intervalo (25,50]")
if 50 < A <= 75:
    print("Intervalo (50,75]")
if 75 < A <= 100:
    print("Intervalo (75,100]")
