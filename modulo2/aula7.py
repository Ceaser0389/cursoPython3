"""
Escopo de 3 funçoes de Python
Escopo significa o local onde aquele codico pode atigir
Esxiste o escopo global e local.
O escopo global e o escopo onde e alcan
o escopo local e o esc onde apenasnomes do mesmo local
"""

# escopo global
x=1

def escopo():
    # escopo local
    x =10
    def outra_funcao():
      y=2
      print(x,y)
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)


