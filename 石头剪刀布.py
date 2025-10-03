import random

b = ["剪刀", "石头", "布"]
win_list = [["石头", "剪刀"], ["剪刀", "布"], ["布", "石头"]]

while True:
    a = input("请出（石头、剪刀、布，输入'退出'结束游戏）：")

    if a == "退出":
        print("游戏结束！")
        break

    if a in b:
        mac = random.choice(b)
        print("你出的是：", a)
        print("计算机出的是：", mac)

        if a == mac:
            print("平局")
        elif [a, mac] in win_list:
            print("恭喜你，你赢了！")
        else:
            print("很遗憾，你输了！")
        print(a,mac,sep='|',end='*'*20)
    else:
        print("输入错误！请输入'石头'、'剪刀'或'布'")