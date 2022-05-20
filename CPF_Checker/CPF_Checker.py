import os
os.system('cls')

val_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]  # Lista de validação do primeiro dígito
val_2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]  # Lista de validação do segundo dígito
CPF_Input = list(map(int, input('Digite o CPF sem os separadores: ')))

list1 = []  # 1ª lista de validação
list2 = []  # 2ª lista de validação

for i in range(0, 9):  # Multiplica 1ª lista de validação pelo CPF
    i = CPF_Input[i] * val_1[i]
    list1.append(i)

for i in range(0, 10):  # Multiplica 2ª lista do CPF
    i = CPF_Input[i] * val_2[i]
    list2.append(i)

listSum1 = sum(list1) * 10 % 11  # Resto da / para verificar o 1º dígito apos o hífen
listSum2 = sum(list2) * 10 % 11  # Resto da / para verificar o 2º dígito apos o hífen

# Verifica CPF's invalidos conhecidos Ex: 111.111.111-11
if CPF_Input[0] == CPF_Input[1] and CPF_Input[1] == CPF_Input[2] and CPF_Input[2] == CPF_Input[3]:
    print(f"\nO CPF: {''.join(map(str, CPF_Input))} não é valido!\n")

# Verifica se o CPF é valido
elif listSum1 == CPF_Input[9] and listSum2 == CPF_Input[10]:
    print(f"\nO CPF: {''.join(map(str, CPF_Input))} é valido!\n")
    
# Retorno do CPF invalido!
else:
    print(f"\nO CPF: {''.join(map(str, CPF_Input))} não é valido!\n")

# Fim
