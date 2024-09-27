n = int(input("digite um numero: "))

def fib(x):
    seq = [0, 1]

    while seq[-1] < n:
        valor = seq[-1] + seq[-2]
        seq.append(valor)

    if x in seq:
        return (f"O valor {x} faz parte da sequencia de fibonacci")
    else:
        return (f"o valor {x} não faz parte da sequencia de fibonacci")
    
res = fib(n)
print(res)


