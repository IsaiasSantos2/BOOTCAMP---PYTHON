from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
arrayShift = ['']
print(logo)
print('A Cifra de César, também conhecida como cifra de troca, é uma das mais simples e conhecidas técnicas de criptografia. Foi utilizada por Júlio César para proteger comunicações militares, daí o nome. A ideia por trás da Cifra de César é substituir cada letra do texto original por outra letra que esteja localizada um número fixo de posições à frente no alfabeto. Por exemplo, se você escolher um deslocamento de 3, cada letra "A" seria substituída por "D", "B" por "E", "C" por "F", e assim por diante. Se a letra estiver no final do alfabeto, ela volta para o início. Por exemplo, "X" seria substituído por "A" (deslocamento de 3).')

def césar():
        if var == False: #criptografar
            word = input("Qual palavra deseja criptografar? ").lower()  
            shift = int(input("Qual o grau de criptografia? "))
            if shift > 26:
                print("O grau é grande demais")
                return césar()
            arrayShift = alphabet[shift:] + alphabet[:shift]
            mapeamento = dict(zip(alphabet, arrayShift))
            string = ""
            for letra in word:
                if letra in mapeamento:
                    string += mapeamento[letra]
                else:
                    string += letra
            print(string)
            if input("Deseja continuar?(Sim)/(Não)").lower() == "sim":
                césar()
            else: exit()

        elif var == True:
            string = ""
            word = input("Qual palavra deseja descriptografar? ").lower()  
            shift = int(input("Qual o grau de descriptografia? "))
            if shift > 26:
                print("O grau é grande demais")
                return césar()
            arrayShift = alphabet[shift:] + alphabet[:shift]
            map = dict(zip(arrayShift, alphabet))
            for letra in word:
                if letra in map:
                    string += map[letra]
                else:
                    string += letra
                    break
            print(string)
            if input("Deseja continuar?(Sim)/(Não)").lower() == "sim":
                césar()
            else: 
                print("Obrigado pela sua atenção ^^")
                exit()

var = int(input("Deseja criptografar ou descriptografar uma palavra?(1/2)"))
if var == 1:
    var = False
    césar()
elif var == 2: 
    var = True
    césar()