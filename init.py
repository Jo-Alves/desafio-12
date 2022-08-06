"""
Jardeclenio é um empresário dono de um Zoológico e precisa
de um programa para cadastrar os seus animais
Faça um programa que persista dos dados dos animais no disco

Exemplo do escopo da classe
Animal
    ##### propriedades #####
    - codigo
    - nome
    - descricao

    ##### metodos #####
    - gravar()
    - buscar()
    - mostrar()
"""


import controller.animal_controllers as animal

print("=" * 30 + " [Menu] " + "=" * 30 + "\n")
print("0 - Sair")
print("1 - Gravar")
print("2 - Mostrar")
print("3 - Buscar\n")
print("=" * 68 + "\n")

while True:
    opcao = input()
    if(opcao == "0"):
        break
    elif(opcao == "1"):
        animal.gravar()
        break
    elif(opcao == "2"):
        animal.buscar()
        break
    elif(opcao == "3"):
        animal.buscar_por_Codigo()
        break