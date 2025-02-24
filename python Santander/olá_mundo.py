print ("Olá Mundo!")

#IF,ELIF,ELSE

idade = 18
if idade == 18:
    print ("Você atingiu a maioridade.")
elif idade >= 18 and idade < 65:
    print ("Adulto")
elif idade >= 65:
    print ("Idoso")
else:
    print ("Você é menor de idade.")

   
nota = 70
if nota >= 90:
   print ("Excelente")

elif nota >= 80:
   print ("Muito bom")

elif nota >= 70:
   print ("Bom")

elif nota >= 50:
    print ("Na média")
else:
   print ("Precisa melhorar")

#LOOPS

#FOR
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)


for i in range(1, 101): #onde termina o range, que é o espaço determinado, você sempre coloca um valor a mais de onde termina
    print(i)

#WHILE
contador = 0
while contador <=5:

    print(contador)
    contador += 1