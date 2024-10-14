def cor(lista):
    esque = 0
    dire = 0
    listaZero = []
    listaLapis = []
    
    for i in range(len(lista)):
        if lista[i] == 0:
            listaZero.append(i)




    for i in range(len(lista)):
        esque = 0
        dire = 0
        if lista[i] != 0:
            m = 9
            for z in listaZero:
                
                d = i-z
                print(m, d)
                if d < 0:
                    d*=-1
                if d < m:
                     m = d
            lista[i]=m
            
                    
                
            
        
            
                        
        



                    

               
                     




lapis = [-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1, 0, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
cor(lapis)
print(lapis)

