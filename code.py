from typing import List
def pyramid():
    n = int(input())
    aux = n
    respuesta = 1
    altura = 1
    if(n<2):
        respuesta = 0
    while(aux>=2):
        aux = aux - 2*altura - altura + 1
        if( aux < 0 ):
            aux = aux + 2*altura + altura - 1
            altura = 1
            respuesta = respuesta + 1
        else:
            altura = altura + 1
    print(respuesta)
t = int(input())
for i in range(t):
    pyramid()