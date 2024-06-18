import random
word_list = ["ardvark", "baboon", "camel"]
def principal(
):
    x = random.randrange(0,3)
    print("O jogo começou!")
    palavracorreta  = [letra for letra in word_list[x]]
    palavracorreta = ''.join(palavracorreta)
    print(palavracorreta) 

    y = input("Adivinhe a palavra: ")
    letrinha = ""

#enumerate(
    if y == palavracorreta:
        print("This is correct!")
        
    else:
        
     palavracorreta = [letra for letra in word_list[x]]
     palavraerrada = [letra for letra in y]
    
    for i, letra_correta in enumerate(palavracorreta):
        letra_errada = palavraerrada[i]
        
        if letra_errada == letra_correta:
            print("Correct")
            Jogar = input("Deseja jogar novamente?(S/N)")
            if Jogar == "S":
                 principal()
            else: print("Programa encerrado.")
        else:
            print("wrong")
            Jogar = input("Deseja jogar novamente?(S/N)")
            if Jogar == "S":
                principal()
            else: print("Programa encerrado.")
     
Iniciar = input("Iniciar programa?(S/N)")
if Iniciar == "S":
    principal()
    
            
        
    
 
    
     
   