# #1 - Crie uma condição para comparar idades: 45 e 18 -  QUAL É MENOR E QUAL É MAIOR?  ----- AULA 03

# a = 45
# b = 18
# if(a > b): # Se
#   print('É maior', a) #true

# else:       # Senão
#   print('É menor'. b) #false


# #2 - Crie um sistema para permitir a verificação de menores em um show  ----- AULA 03

# idade = int(input('Qual a sua idade? '))

# if(idade > 18): # Se
#   print('Acesso permitido', idade) #true

# else:       # Senão
#   print('Acesso negado', idade) #false

# #3 - Crie um algoritmo que permita a entrada de 3 notas de alunos, utilize o bloco de código if()**  ----- AULA 03

# nota1 = int(input('Digite sua primeira nota: '))
# nota2 = int(input('Digite sua segunda nota: '))
# nota3 = int(input('Digite sua terceira nota: '))
# nota = ((nota1 + nota2 + nota3) / 3)

# if( nota >= 6): # Se
#    print('Aprovado', nota) #true

# else:       # Senão
#   print('Reprovado', nota) #false



# #-----------------------------------------SINAIS DE COMPARAÇÃO ----- AULA 04 ---------------------------------------------------------------------------

# n1 = 10

# if n1 == 10 and m1 > 11:
#   print("ok")

# # AND = 2 expressões precisa ser verdadeiras

# if n1 > 1 or n1 >= 2:
#   print("É maior")

# # OR = tanto faz, qualquer umas delas, podem ser verdadeiras

# if not n1 == 1:
#   print("não é igual")

# # NOT é igual == not precisa ser falsa para ser verdadeira


# #------------------------------------CONCATENAÇÃO DE STRING

# num1 = 10
# num2 = 'hello'

# #textos e números
# print(num1, num2)

# #textos e números
# print(f'{num1}{num2}')

# #Com números reais
# print('Hello %s %s'%(num1,num2))

# #com números reais e textos
# print("Hello {}{}".format(num1,num2))


# #-------------------------  Condicionais


# # 1: Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.

# frase = 'Frase para testar programa da aula '
# palavra = input('Digite uma palavra: ')
# print(f'{frase}{palavra}')


# # Exercício 1: Verificação de Número Positivo
# # Escreva um programa em Python que solicite ao usuário um número inteiro e verifique se o número é positivo, negativo ou zero. Em seguida, exiba uma mensagem apropriada de acordo com o resultado da verificação.

# numero = int(input('Digite um número inteiro: '))

# if numero > 0:
#   print('Maior que zero')

# elif numero == 0:
#   print('Zero')

# else:
#   print('Menor que zero')


# # Exercício 2: Classificação de Triângulos
# # Escreva um programa em Python que receba três comprimentos de lados de um triângulo e determine se o triângulo é equilátero, isósceles ou escaleno.

# # Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# # Triângulo Equilátero: três lados iguais;
# # Triângulo Isósceles: quaisquer dois lados ig1uais;
# # Triângulo Escaleno: três lados diferentes;


# lado1 = int(input('Digite o primeiro lado: '))
# lado2 = int(input('Digite o primeiro lado: '))
# lado3 = int(input('Digite o primeiro lado: '))

if lado1 == lado2 and lado2 == lado3:  #lado3 == lado2 == lado3
  print('Triângulo Equilátero')

elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1: 
  print('Triângulo Isósceles')

elif lado1 != lado2 and lado2 != lado3 and lado3  != lado1: #lado1 != lado2 != lado3
  print('Triângulo Escaleno')


# Exercício 3: Verificação de Ano Bissexto
# Um ano é bissexto se for divisível por 4, exceto para anos que são divisíveis por 100. No entanto, anos divisíveis por 400 também são bissextos. 
# Escreva um programa em Python que solicite um ano ao usuário e determine se é um ano bissexto ou não.

ano = int(input('Ano: '))
if (ano % 4 == 0 or ano % 100 == 0) or (ano % 400 == 0):
  print("O ano é bissexto")
else:
  print("Não é bissexto")
