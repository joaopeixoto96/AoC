import os
file_path = os.path.join('AoC_2023','day1.txt')
file_input = open(file_path)

data = [i for i in file_input.read().strip().split()]

p1 = 0
p2 = 0

for item in data:
    p1_digits = [] 
    p2_digits = []

    for index, c in enumerate(item):
        if c.isdigit():
            p1_digits.append(c)
            p2_digits.append(c)
            
        for digit, value in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
            if item[index:].startswith(value):
                p2_digits.append(str(digit+1))

    p1 += int(p1_digits[0] + p1_digits[-1])
    p2 += int(p2_digits[0] + p2_digits[-1])

print(f'Parte 1 -> {p1} e Parte 2 -> {p2}')


'''Primeira tentativa'''
#No fundo na primeira tentativa a ideia foi ir linha a linha procurar
#os numeros e guarda-los associados à linha de onde vinham. Depois noutro ciclo
# era preciso tirar o espaço entre o primeiro e o ultimo numero para que formasse 
# um número só. Finalmente somar os elementos todos da lista. 
#Para simplificar este código todo, simplesmente adicionei ao codigo da parte 2
#as linhas que têm p1

# calib = []
# for item in data:
#     val = []
#     for ele in item:
#         if ele.isnumeric():
#             val.append(ele)
#     calib.append(val)
# print(calib)

# numeros = []
# for item in calib:
#     rasco = item[0],item[-1]
#     delim=''
#     result = delim.join(rasco)
#     numeros.append(result)

# soma = 0
# for item in numeros:
#     soma += int(item)

# print(soma)