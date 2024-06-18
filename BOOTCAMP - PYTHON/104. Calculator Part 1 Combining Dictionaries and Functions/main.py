from functools import reduce
operations = ["+","-","*","/"]
controler = True
for operation in operations:
    print(operation)
while controler == True:
    operação = input("Qual é a operação que você quer fazer? ")
    if operação == "+":
        valores = (input("Digite os valores separado por espaço "))
        valores = valores.split()
        valores = [float(valor) for valor in valores]
        resultado = sum(valores)
        print("Resultado da soma: ", resultado)
        controler = False
    if operação == "-":
        valores = (input("Digite os valores separado por espaço "))
        valores = valores.split()
        valores = [float(valor) for valor in valores]
        resultado = reduce(lambda x, y: x - y, valores)
        print("Resultado da subtração: ", resultado)
        controler = False
    if operação == "*":
        valores = (input("Digite os valores separado por espaço "))
        valores = valores.split()
        valores = [float(valor) for valor in valores]  
        resultado = reduce(lambda x, y: x * y, valores)
        print("Resultado da multiplicação: ", resultado)
        controler = False
    if operação == "/":
        valores = (input("Digite os valores separado por espaço "))
        valores = valores.split()
        valores = [float(valor) for valor in valores]  
        resultado = reduce(lambda x, y: x / y, valores)
        print("Resultado da divisão: ", resultado)   
        controler = False
    while controler == False:
     continuar = input("Gostaria de fazer outro cálculo? (s/n): ")
     if continuar.lower() != "s":  
            controler == False
            
          
