a = 'a'
a2 = "A"
qtd = 0

seq = str(input("Digite sua sequencia de string: "))

seq2 = list(seq)
for i in range(len(seq2)):
    if seq2[i] == a or seq2[i] == a2:
        qtd = qtd + 1

if(qtd > 0):
    print("Tem A letra a na string")

print(qtd)