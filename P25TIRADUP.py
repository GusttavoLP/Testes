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
def locdup (V,f,V2):
    print(f)
    M=0
    V2=[]
    for i in range (1,(len(V)-1),1):
        if(V(i)==V(M)):
            V2.append(i)
        else:
            M=M+1
    return( )
#
#BOAS VINDAS
print("Bem vindo, Sr. usuário!")
print("PROGRAMA ELIMINA DUPLICATAS DE UM VETOR")
print(" ")
#
#DIÁLOGO DE ENTRADA DE DADOS
X=gervetint(99,200,400,"Gerando vetor X.")
print("Vetor X gerado com",len(X),"elementos:\n",X)
#
#PROCESSAMENTO
locdup(X,"Procurando duplicatas em X...",X2)
print("As duplicatas de X estão localizadas nas posições:\n",X2)
while (len(X2))>1:                         #enquanto houverem duplicatas
    for i in range (len(X2),1,-1):
        X.pop(X2[i])                       #Remove de X a duplicata da posição
    X2.pop( )                              #Uso de while pois o vetor muda de tamanho
#
#
#EMISSÃO DO RELATÓRIO DE SAÍDA
print("O vetor X continha",(len(X2)-1),"duplicatas.")
print("Vetor X sem duplicatas:\n",X)
print(" ")
#
#DESPEDIDA
print("Execução concluida. Tenha um bom dia!")
print(" ")
#
#TERMINAÇÃO
#Não precisa em python
