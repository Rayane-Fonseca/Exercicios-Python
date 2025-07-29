#esse vai pedir ao usuário os números

num1 = int (input("Digite o primeiro número: "))
num2 = int (input("Digite o segundo número: "))
num3 = int (input("Digite o terceiro número: "))

print (f"{num1}, {num2}, {num3}")

if num1 < num2 > num3:
    print (f"O número {num2} é o maior")
elif num1 > num2 < num3:
    print (f"O número {num1} é o maior")
else: #num1 < num2 < num3:
    print (f"O número {num3} é o maior")

#esse já tem os números armazenados dentro do código

def maior_de_tres (a, b, c):
    if a >= b and a >= c:
        print (a)
    elif b >= a and b >= c:
        print (b)
    else:
        print (c)

maior_de_tres (10, 20, 30)