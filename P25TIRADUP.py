#P25TIRADUP.py
#UNIVERSIDADE FEDERAL FLUMINENSE
#ESCOLA DE ENGENHARIA - ENGENHARIA AGRÍCOLA E AMBIENTAL
#TCC00326 - PROGRAMAÇÃO DE COMPUTADORES
#TURMA P1 2024/1 PROF.JOHN REED
#PROGRAMADOR: LUCAS THEVENARD SENRA. MAT:120043053
#DATA: 06.05.2024
#P25TIRADUP.py: PROGRAMA ELIMINA DUPLICATAS DE UM VETOR
#
#DESCRIÇÃO DOS OBJETOS
'''P25TIRADUP.py
Faça um programa python elegante, eficiente e bem estruturado que:
a) Escreva uma função para gerar um vetor qualquer, de tamanho qualquer de inteiros, gerados em um intervalo qualquer;
b) Usando a função de a), gere o vetor X com 100 inteiros no intervalo (200,400);
c) Escreva uma função para identificar duplicatas em um vetor;
d) Usando a função de c), elimine as duplicatas de X, deixando apenas a primeira ocorrência da duplicata em X.'''
#X: Vetor com 100 inteiros
def gervetint (n,inic,fin,f):
    print(f)
    from random import randint
    return([randint(inic,fin) for i in range(0,n,1)])
def locdup (V,f):
    print(f)
    V2=[]
    for i in range (0,(len(V)),1):
        naoFoi = True
        for j in range (0,(len(V)),1):
            if((V[i])==(V[j]) and (i!=j) and naoFoi):
                V2.append(i)
                naoFoi = False
    return V2
#
#BOAS VINDAS
print("Bem vindo, Sr. usuário!")
print("PROGRAMA ELIMINA DUPLICATAS DE UM VETOR")
print(" ")
#
#DIÁLOGO DE ENTRADA DE DADOS
X=gervetint(100,200,400,"Gerando vetor X.")
print("Vetor X gerado com",len(X),"elementos:\n",X)
#
#PROCESSAMENTO
X2 = locdup(X,"Procurando duplicatas em X...")
print("As duplicatas de X estão localizadas nas posições:\n",X2)      
qtdDup = len(X2)
X3 = X.copy()
X4 = []
i = (len(X2)-1)
while (len(X2))>0:                          #enquanto houverem duplicatas
    X3.pop(X2[i])                           #Remove de X a duplicata da posição
    if (len(X4)!=0):
        jaTem = False
        for j in range (0,(len(X4)),1):         #percorre X4 para saber se já registrou aquela duplicata
            if (X[X2[i]]==(X4[j])):             #se ja tiver a primeira ocorrencia registrada ele não registra
                jaTem = True
        if not(jaTem):
            X4.append(X[X2[i]])                 #se não tiver registrado, registra
    else:
        X4.append(X[X2[i]])                     #primeiro registro sempre é feito
    X2.pop()    
    i -= 1                                  #Uso de while pois o vetor muda de tamanho       
for k in range (0,(len(X4)),1):             #adiciona novamente a primeira ocorrencia de cada duplicata
    X3.append(X4[k])
#
#
#EMISSÃO DO RELATÓRIO DE SAÍDA
print("O vetor X continha", qtdDup,"duplicatas.")
print("Vetor X sem duplicatas:\n",X3)
print(" ")
#
#DESPEDIDA
print("Execução concluida. Tenha um bom dia!")
print(" ")
#
#TERMINAÇÃO
#Não precisa em python
