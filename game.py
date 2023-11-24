import random
import time
# print(time.time())

dict1 = {'♥': 1,
         '♠': 2,
         '♣': 3,
         '♦': 4,
         'j': 5,  # jokers
         'J': 6,
         'p': 0}  # JOKERS

dict2={'2':1,
       '3':2,
       '4':3,
       '5':4,
       '6':5,
       '7':6,
       '8':7,
       '9':10,
       '1':11,  # 10
       'J':12,
       'Q':13,
       'K':14,
       'A':15,
       'o':16,
       'O':17,
       'l': 0}


def is_timestamp():
    print("是否启用时间戳")
    print('1.是    0.否')
    judge = input()
    if judge == '1':
        random.seed(int(time.time()))
    elif judge == '0':
        random.seed(int(input("请输入种子：")))


def rand(list1):
    random.shuffle(list1)

    print('洗牌')
    for i in list1:
        print(i,end=' ')
    print('\n', end='')
    return list1


def init_card():
    point = list(''.join('23456789xJQKA'))
    point[8] = '10'
    # print(point)
    card = []
    for i in ['♥','♠','♣','♦']:
        for j in point:
            card.append(f'{i}{j}')
    card.extend(['jokers','JOKERS'])

    print('新牌')
    for i in card:
        print(i,end=' ')
    print('\n',end='')
    return card


def fapai(card, players):
    player = []
    for i in range(players):
        player.append([f'player{i+1}'])
    num = len(card)

    for i in range(num):
        judge = i % players
        player[judge].append(card[i])

    print("发牌")
    for i in range(players):
        for j in player[i][1:]:
            print(j,end=' ')
        print("\n",end='')

    return player


# def sort_key(card):
#     for i in range(len(card)):


def card_sort(card):
    lenth = len(card)
    for i in range(lenth):
        # print(card[i])
        card[i].sort(key=lambda x: dict2[x[1]])
        card[i].sort(key=lambda x: dict1[x[0]])
        # print(card[i])

    print('排序')
    for i in range(lenth):
        for j in card[i][1:]:
            print(j,end=' ')
        print("\n",end='')

    return card


if __name__ == '__main__':
    card = init_card()
    player = fapai(card, 2)
    ret = card_sort(player)
    # pass
