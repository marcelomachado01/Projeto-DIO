'''
# 1️⃣ Desafio Classificador de nível de Herói

**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões

## Objetivo

Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

Se XP for menor do que 1.000 = Ferro
Se XP for entre 1.001 e 2.000 = Bronze
Se XP for entre 2.001 e 5.000 = Prata
Se XP for entre 6.001 e 7.000 = Ouro
Se XP for entre 7.001 e 8.000 = Platina
Se XP for entre 8.001 e 9.000 = Ascendente
Se XP for entre 9.001 e 10.000= Imortal
Se XP for maior ou igual a 10.001 = Radiante

## Saída

Ao final deve se exibir uma mensagem:
"O Herói de nome **{nome}** está no nível de **{nivel}**"
'''

nomeHeroi = input("Qual o nome do herói: ")
xpHeroi = int(input("Qual o XP do herói: "))

if xpHeroi < 1000 :
   nivel = "Ferro"
elif  1001 <= xpHeroi <= 2000:
   nivel = "Bronze"
elif 2001 <= xpHeroi <= 5000:
   nivel = "Prata"
elif 6001 <= xpHeroi <= 7000:
   nivel = "Ouro"
elif 7001 <= xpHeroi <= 8000:
   nivel = "Platina"
elif 8001 <= xpHeroi <= 9000:
   nivel = "Ascendente"
elif 9001 <= xpHeroi <= 10000:
   nivel = "Imortal"
else:
   nivel = "Radiante"

print("O Herói {} está no nivel {}." .format(nomeHeroi, nivel))