from login import *
from cadastro import *
 
print("Bem vindo ao Obravista")
print("1 login \n2 login")
escolha = int(input(""))

if escolha == 1:
    print("indo pro login")
    login()
    

elif escolha == 2:
    print("indo pro cadastro")
    cadastro()