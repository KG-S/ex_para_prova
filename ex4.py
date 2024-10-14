def remove(f ,l):
    if len(f) != 0:
        if f[-1] == l:
            return f[:-1]
        else:
             return remove(f[:-1],l)+f[-1]


palavra = input("Digite a palavra: ")
letra = input("Digite a letra: ")


print(remove(palavra, letra))

