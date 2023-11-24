from game import *

def menu1():
    print('是否开始游戏：')
    print("1.开始 0.结束")
def menu2():
    print('请设定游戏人数:', end='')
    return int(input())
def Game():
    is_timestamp()
    player_num = menu2()
    card = init_card()
    new_card = rand(card)
    player = fapai(new_card, player_num)
    player = card_sort(player)

    # print(player)
    # for i in range(player_num):
    #     # lenth = len(player[i])
    #     for j in player[i][1:]:
    #         print(j,end=' ')
    #     print("\n",end='')

if __name__ == '__main__':
    menu1()
    get = input()
    if get == "1":
        Game()
    else:
        exit(0)
