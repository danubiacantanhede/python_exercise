#insira um número

num1 = int(input("Escreva um numero "))

num2 = int(input("Escreva outro numero "))

Op= input("Coloque uma operacao")

if "+" in Op:
    print(num1 + num2)

elif  "-" in Op:
    print(num1 - num2)

elif "*" in Op:
    print(num1 * num2)

elif "/" in Op:
    print(num1/num2)

else:
    print ("Operações: soma, subtração, multiplicação e divisão")
    
