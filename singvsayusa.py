import random
sinhp = 100
ayuhp = 100

sinleft = 0
ayuleft = 0

round_number = 1
while sinhp * ayuhp > 0:
    if round_number != 1: print("\n\n")
    print(f"> Round {round_number} - sing {sinhp} vs {ayuhp} アユサ")
    turn = random.randrange(2)
    for i in range(2):
        r = random.random()
        if turn == 0:
            print("\n# singのターン")
            if sinleft > 0:
                sinleft -= 1
                print(f"singは眠っている 残り{sinleft}ターン")
            elif r < 0.05:
                print("singは酒を使った！アユサは酒に溺れた！")
                ayuhp = 0
                break
            elif r < 0.25:
                print("singのねむる!singはHPを全回復した!!眠ってしまい3ターン休み!!!")
                sinhp = 100
                sinleft += 3
            else:
                print("singの環状線アタック！アユサに10のダメージ！")
                ayuhp -= 10
        else:
            print("\n# アユサのターン")
            if ayuleft > 0:
                ayuleft -= 1
                print(f"アユサは火麒麟で暴れている 残り{ayuleft}ターン")
            elif r < 0.3:
                print("アユサの火麒麟！アユサはHPを全回復した!!楽しくなって3ターン休み!!!")
                ayuhp = 100
                ayuleft += 3
            else:
                dmg = random.randrange(47)
                print(f"アユサのえ゛え゛ど゛ね゛!!!singに{dmg}ダメージ!!!")
                sinhp = max(0, sinhp-dmg)
        if sinhp * ayuhp <= 0: break
        turn = (turn + 1) % 2
    round_number += 1

if sinhp == 0: print("\n\nアユサの勝ち!!")
else: print("\n\nsingの勝ち!!")
