def matriz(m):
    matrizOK = True
    if len(m) % 2 == 0:
        matrizOK = False
    for i in m:
        if len(i) != len(m):
            matrizOK = False

    if matrizOK == False:
        return m
    else:
        mnovo = []
        centro = int((len(m)-1)/2)
        c2=centro+1
        
        linha = m[(centro)]
        
        l2 = []
        for i in range(len(m)):
            
            if i != centro:
                for c in range(len(m[i])):
                    if c == (centro):
                        if len(mnovo) < (i+1):
                            mnovo.append([])
                        l2.append(m[i][c])
                        
                        mnovo[i].append(linha[i])
                    else:
                        if len(mnovo) < (i+1):
                            mnovo.append([])
                        
                        mnovo[i].append(m[i][c])
            else:
                l2.append(linha[i])
                
                mnovo.append([])
                        
                
    mnovo[centro] = l2           
                
    return mnovo
                



matrix = [[0,1,2,3,4,4,4],[0,1,2,3,4,4,4],[0,1,2,3,4,4,4],[5,6,7,8,9,4,2],[0,4,0,0,0,0,2],[0,1,4,2,3,4,4],[5,6,4,7,8,9,4]]
for o in matrix:
    print(o)

print()

x = matriz(matrix)

for o in x:
    print(o)

