from models.animal import Animal
from time import sleep
from os import system

animal = Animal()

def gravar():
    while True:
        system("clear")
        print("=" * 50)
        while True:
            animal.nome = input("Digite o nome do animal:\n")
            if animal.nome:
                break

            print("O nome está vazio. Digite o nome.")
            sleep(.5)
            system("clear")
        print("=" * 50)
        animal.descricao = input("Digite a descrição do animal:\n")
        print("=" * 50)
        animal.gravar()
        
        opçao = input("Deseja gravar mais um animal? [S|N]\n")
        if  opçao.lower() == "n":
            break
        sleep(.8)

def buscar():
    system("clear")
    animais = Animal.buscar()
    
    if len(animais) == 0:
        print("Não há animais cadastrados.")
        return
        
    for animal in animais:
        print("=" * 50)
        print(f"Código: {animal.codigo}")
        print(f"Nome: {animal.nome}")
        print(f"Descrição: {animal.descricao}")
        sleep(.7)

        
def buscar_por_Codigo():
    system("clear")
    while True:
        codigo = input("Digite o código do animal: ")
        if codigo:
           break 
       
        print("O código está vazio. Digite o código do animal.")
        sleep(.7)
        system("clear")
        
    animal = Animal.buscar_por_codigo(codigo)
    if animal == None:
        print("Não achamos um animal com este código.")
        return
    
    sleep(.5)   
    print("=" * 50)
    print(f"Código: {animal.codigo}")
    print(f"Nome: {animal.nome}")
    print(f"Descrição: {animal.descricao}")
    sleep(.8)   