"""
Escopo de funções em Python
escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o esc onde td o código é alcançavel
o escp local é o escp onde apen nomes do mesmo local
podem ser alcançados
"""

x = 1

def escopo():
    global  x
    x = 10
    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x,y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x)