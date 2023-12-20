import os
file_path = os.path.join('AoC_2023','day4.txt')
with open(file_path, 'r') as f:
    lines = f.readlines()
    cards = [entry.strip() for entry in lines]


total_point_list = []
p2 = [1] * len(cards)

for idx, line in enumerate(cards): 
    game_info = line.split(':')[-1].split('|')
    set_1 = set(map(int, game_info[0].split()))
    set_2 = set(map(int, game_info[1].split()))
    repeated_cards = set_1.intersection(set_2)
    num_repeated_cards = len(repeated_cards)

    if num_repeated_cards > 0:
        pontos = 1
        for i in range(num_repeated_cards):
            if i == num_repeated_cards - 1:
                break
            else:
                pontos *= 2
                i += 1
        
        total_point_list.append(pontos)
    else:
        pontos = 0
        total_point_list.append(pontos)

    for i in range(num_repeated_cards):
        p2[idx + i + 1] += p2[idx]

print('Sol Part 1 -',sum(total_point_list))
print('Sol Part 2 -',sum(p2))

#Aqui está a solução independente da parte 1 que entretanto consegui integrar
#na nova solução da parte 2 ficando só um ciclo para as duas
#Tive que mudar a forma como corria a linha a linha para ter acesso aos indices
#para finalmente conseguir adicionar as linhas pelo meio.
#Esta solução é bem tricky e não tinha conseguido se não visse um macaco no reddit a complicar

# '''Part 1'''
# total_point_list = []
# for item in cards:
#     # card_number = item.split()[1].strip(':') # inutil acho eu
#     game_info = item.split(':')[-1].split('|')
#     set_1 = set(map(int, game_info[0].split()))
#     set_2 = set(map(int, game_info[1].split()))
#     repeated_cards = set_1.intersection(set_2)
#     num_repeated_cards = len(repeated_cards)

#     if num_repeated_cards > 0:
#         pontos = 1
#         for i in range(num_repeated_cards):
#             if i == num_repeated_cards - 1:
#                 break
#             else:
#                 pontos *= 2
#                 i += 1
        
#         total_point_list.append(pontos)
#     else:
#         pontos = 0
#         total_point_list.append(pontos)

# print(sum(total_point_list))
