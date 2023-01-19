Entrada = input().split()
A = float(Entrada[0])
B = float(Entrada[1])
C = float(Entrada[2])
D = float(Entrada[3])
E = ((A*2)+(B*3)+(C*4)+(D*1))/10
print("Media: %.1f" % E)
if E < 5.0:
    print("Aluno reprovado.")
if E >= 7.0:
    print("Aluno aprovado.")
if 5 <= E < 7.0:
    print("Aluno em exame.")
    F = float(input())
    print("Nota do exame: %.1f" % F)
    G = (F + E)/2
    if G >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % G)
    
