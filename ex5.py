def remove(l1,l2):
    if len(l1) != 0:
        if l1[0] in l2:
            return remove(l1[1:],l2)
        else:
            
            return [l1[0]] + remove(l1[1:],l2)
    else:
        return []

lista1= [21, 9, 35, 9, 43, 7]
lista2= [7, 9, 8]
print(remove(lista1,lista2))
