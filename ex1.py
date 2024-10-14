def listAluno(a,nome):
   
    ml = []

    for i in range(0,len(a[nome[1]])):
        if a[nome[1]][i][0] not in ml:
            ml.append(a[nome[1]][i][0])
            soma = 0
            conta = 0
            for l in a[nome[1]]:
                
                if l[0] == a[nome[1]][i][0]:
                   
                    soma+=l[2]
                    conta+=1
            ml.append(soma/conta)
        
    return ml
    
def DisciplinaNota(d, n):
    maior = []
    indice = 0
    for i in range(len(n)):
        
        for y in range(len(n[i])):
            
            if n[i][y][0] == d:
                if len(maior) != 0:
                   
                    if maior[0][0] < n[i][y][2]:
                        maior =[[ n[i][y][2], i]]
                        
                    elif maior[0][0] == n[i][y][2]:
                        if i != maior[0][1]:
                            maior.append([n[i][y][2], i])
                else:
                    maior =[[ n[i][y][2], i]]
                    
    
    return(maior)
                    
                       
                       
    






 #Programa Principal
 # lista com nomes e idades dos alunos
Alunos=[  ['João Pedro Souza', 18], ['Isabela Moraes', 17], ['Daniel Silva', 19]  ]
 # notas dos alunos – código da disciplina, nome da prova e nota
Notas = [ [  ['MAT', 'P1', 5.8], ['ALG', 'P1', 7.4], ['WEB', 'P1', 8.9], ['ALG', 'P2', 9.6] ],   # provas do João
          [  ['ALG', 'P1', 9.2], ['WEB', 'P1', 6.7], ['WEB', 'P2', 9.3] ],   # provas da Isabela
          [['MAT', 'P1', 5.8], ['ALG', 'P1', 9.6], ['MAT', 'P2', 8.1], ['MAT', 'P3', 8.1]
          ]]  # provas do Daniel]   # fecha a lista de notas


for i in range(0,len(Alunos)):
    print(i, "-",Alunos[i][0])
x=int(input("digite o numero do aluno que vc quer ver: "))
x=[Alunos[x][0], x]
p = listAluno(Notas,x)


for y in range(0, len(p),2):
    print("Disciplina: ", p[y]," Média: ", p[y+1])


r=input("Digite a discilina: ")
resultado = DisciplinaNota(r, Notas)

for f in resultado:
    
    print("Aluno: ", Alunos[f[1]][0])
    print("Idade: ", Alunos[f[1]][1])
    print("Disciplina: ",r)
    print("Nota: ",f[0])
    print()
