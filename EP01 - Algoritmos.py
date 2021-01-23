'''
+---------------------------------------------------------------------------------------+
| Instituiçao   :    Faculdade de Técnologia de São Paulo                               |
| Departamento  :    Tecnologia da Informação                                           |
| Curso         :    Analise e Denvolvimento de Sistemas			        |
| Turma         :    Vespertino	                                                        |
| Aluno         :    Artur Caetano e Guilherme Caetano          			|
| Matricula     :                                               		        |
+---------------------------------------------------------------------------------------+
| Programa	:    EP01.py - ordem_inversa                                            |
| Linguagem	:    Python 3                                                           |
| Compilador	:    IDLE Version 3.6.5                                                 |
+---------------------------------------------------------------------------------------+
'''


def ordem_inversa(a, b, n):
    condicao = True
    for i in range(n):        
        if(a[i]!=b[n-i-1]and condicao == True):            
            print("a[", i , "] = ", a[i])
            print("b[", n-i-1 , "] = ", b[n-i-1])
            condicao=False
    if(condicao == True):
        print("ordem inversa")

        
n = int(input("Digite o tamanho do vetor\n"))
a = [0]*n
b = [0]*n
for i in range(n):
  a[i] = int(input("Digite um numero para armazenar no vetor A \n"))

for l in range(n):
  b[l] = int(input("Digite um numero para armazenar no vetor B \n"))

ordem_inversa(a, b, n)
